# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from code import Code
from model import PropertyType, Property, Type
import cpp_util
import schema_util
import util_cc_helper
from cpp_namespace_environment import CppNamespaceEnvironment

class CCGenerator(object):
  def __init__(self, type_generator):
    self._type_generator = type_generator

  def Generate(self, namespace):
    return _Generator(namespace, self._type_generator).Generate()


class _Generator(object):
  """A .cc generator for a namespace.
  """
  def __init__(self, namespace, cpp_type_generator):
    assert type(namespace.environment) is CppNamespaceEnvironment
    self._namespace = namespace
    self._type_helper = cpp_type_generator
    self._util_cc_helper = (
        util_cc_helper.UtilCCHelper(self._type_helper))
    self._generate_error_messages = namespace.compiler_options.get(
        'generate_error_messages', False)

  def Generate(self):
    """Generates a Code object with the .cc for a single namespace.
    """
    cpp_namespace = cpp_util.GetCppNamespace(
        self._namespace.environment.namespace_pattern,
        self._namespace.unix_name)

    c = Code()
    (c.Append(cpp_util.CHROMIUM_LICENSE)
      .Append()
      .Append(cpp_util.GENERATED_FILE_MESSAGE %
              cpp_util.ToPosixPath(self._namespace.source_file))
      .Append()
      .Append('#include "%s/%s.h"' %
              (cpp_util.ToPosixPath(self._namespace.source_file_dir),
               self._namespace.short_filename))
      .Append()
      .Append('#include <memory>')
      .Append('#include <ostream>')
      .Append('#include <string>')
      .Append('#include <utility>')
      .Append('#include <vector>')
      .Append()
      .Append('#include "base/check.h"')
      .Append('#include "base/check_op.h"')
      .Append('#include "base/notreached.h"')
      .Append('#include "base/strings/string_number_conversions.h"')
      .Append('#include "base/strings/utf_string_conversions.h"')
      .Append('#include "base/values.h"')
      .Append(self._util_cc_helper.GetIncludePath())
      .Cblock(self._GenerateManifestKeysIncludes())
      .Cblock(self._type_helper.GenerateIncludes(include_soft=True))
      .Append()
      .Append('using base::UTF8ToUTF16;')
      .Append()
      .Concat(cpp_util.OpenNamespace(cpp_namespace))
    )
    if self._namespace.properties:
      (c.Append('//')
        .Append('// Properties')
        .Append('//')
        .Append()
      )
      for prop in self._namespace.properties.values():
        property_code = self._type_helper.GeneratePropertyValues(
            prop,
            'const %(type)s %(name)s = %(value)s;',
            nodoc=True)
        if property_code:
          c.Cblock(property_code)
    if self._namespace.types:
      (c.Append('//')
        .Append('// Types')
        .Append('//')
        .Append()
        .Cblock(self._GenerateTypes(None, self._namespace.types.values()))
      )
    if self._namespace.manifest_keys:
      (c.Append('//')
        .Append('// Manifest Keys')
        .Append('//')
        .Append()
        .Cblock(self._GenerateManifestKeys())
      )
    if self._namespace.functions:
      (c.Append('//')
        .Append('// Functions')
        .Append('//')
        .Append()
      )
    for function in self._namespace.functions.values():
      c.Cblock(self._GenerateFunction(function))
    if self._namespace.events:
      (c.Append('//')
        .Append('// Events')
        .Append('//')
        .Append()
      )
      for event in self._namespace.events.values():
        c.Cblock(self._GenerateEvent(event))
    c.Cblock(cpp_util.CloseNamespace(cpp_namespace))
    c.Append()
    return c

  def _GenerateType(self, cpp_namespace, type_):
    """Generates the function definitions for a type.
    """
    classname = cpp_util.Classname(schema_util.StripNamespace(type_.name))
    c = Code()

    if type_.functions:
      # Wrap functions within types in the type's namespace.
      (c.Append('namespace %s {' % classname)
        .Append())
      for function in type_.functions.values():
        c.Cblock(self._GenerateFunction(function))
      c.Append('}  // namespace %s' % classname)
    elif type_.property_type == PropertyType.ARRAY:
      c.Cblock(self._GenerateType(cpp_namespace, type_.item_type))
    elif type_.property_type in (PropertyType.CHOICES,
                                 PropertyType.OBJECT):
      if cpp_namespace is None:
        classname_in_namespace = classname
      else:
        classname_in_namespace = '%s::%s' % (cpp_namespace, classname)

      if type_.property_type == PropertyType.OBJECT:
        c.Cblock(self._GeneratePropertyFunctions(classname_in_namespace,
                                                 type_.properties.values()))
      else:
        c.Cblock(self._GenerateTypes(classname_in_namespace, type_.choices))

      (c.Append('%s::%s()' % (classname_in_namespace, classname))
        .Cblock(self._GenerateInitializersAndBody(type_))
        .Append('%s::~%s() = default;' % (classname_in_namespace, classname))
      )
      # Note: we use 'rhs' because some API objects have a member 'other'.
      (c.Append('%s::%s(%s&& rhs) = default;' %
                    (classname_in_namespace, classname, classname))
        .Append('%s& %s::operator=(%s&& rhs) = default;' %
                    (classname_in_namespace, classname_in_namespace,
                     classname))
      )

      if type_.origin.from_manifest_keys:
        c.Cblock(
          self._GenerateManifestKeyConstants(
            classname_in_namespace, type_.properties.values()))

      if type_.origin.from_json:
        c.Cblock(self._GenerateTypePopulate(classname_in_namespace, type_))
        if cpp_namespace is None:  # only generate for top-level types
          c.Cblock(self._GenerateTypeFromValue(classname_in_namespace, type_))
      if type_.origin.from_client:
        c.Cblock(self._GenerateTypeToValue(classname_in_namespace, type_))

      if type_.origin.from_manifest_keys:
        c.Cblock(
          self._GenerateParseFromDictionary(
            classname, classname_in_namespace, type_))
    elif type_.property_type == PropertyType.ENUM:
      (c.Cblock(self._GenerateEnumToString(cpp_namespace, type_))
        .Cblock(self._GenerateEnumFromString(cpp_namespace, type_))
      )

    return c

  def _GenerateInitializersAndBody(self, type_):
    items = []
    for prop in type_.properties.values():
      t = prop.type_

      real_t = self._type_helper.FollowRef(t)
      if real_t.property_type == PropertyType.ENUM:
        namespace_prefix = ('%s::' % real_t.namespace.unix_name
                            if real_t.namespace != self._namespace
                            else '')
        items.append('%s(%s%s)' % (prop.unix_name,
                                   namespace_prefix,
                                   self._type_helper.GetEnumNoneValue(t)))
      elif prop.optional:
        continue
      elif t.property_type == PropertyType.INTEGER:
        items.append('%s(0)' % prop.unix_name)
      elif t.property_type == PropertyType.DOUBLE:
        items.append('%s(0.0)' % prop.unix_name)
      elif t.property_type == PropertyType.BOOLEAN:
        items.append('%s(false)' % prop.unix_name)
      elif (t.property_type == PropertyType.ANY or
            t.property_type == PropertyType.ARRAY or
            t.property_type == PropertyType.BINARY or
            t.property_type == PropertyType.CHOICES or
            t.property_type == PropertyType.OBJECT or
            t.property_type == PropertyType.FUNCTION or
            t.property_type == PropertyType.REF or
            t.property_type == PropertyType.STRING):
        # TODO(miket): It would be nice to initialize CHOICES, but we
        # don't presently have the semantics to indicate which one of a set
        # should be the default.
        continue
      else:
        raise TypeError(t)

    if items:
      s = ': %s' % (',\n'.join(items))
    else:
      s = ''
    s = s + ' {}'
    return Code().Append(s)

  def _GenerateTypePopulate(self, cpp_namespace, type_):
    """Generates the function for populating a type given a pointer to it.

    E.g for type "Foo", generates Foo::Populate()
    """
    classname = cpp_util.Classname(schema_util.StripNamespace(type_.name))
    c = Code()
    (c.Append('// static')
      .Append('bool %(namespace)s::Populate(')
      .Sblock('    %s) {' % self._GenerateParams(
          ('const base::Value& value', '%(name)s* out'))))

    if self._generate_error_messages:
      c.Append('DCHECK(error);')

    if type_.property_type == PropertyType.CHOICES:
      for choice in type_.choices:
        (c.Sblock('if (%s) {' % self._GenerateValueIsTypeExpression('value',
                                                                    choice))
            .Concat(self._GeneratePopulateVariableFromValue(
                choice,
                '(&value)',
                'out->as_%s' % choice.unix_name,
                'false',
                is_ptr=True))
            .Append('return true;')
          .Eblock('}')
        )
      (c.Concat(self._AppendError16(
          'u"expected %s, got " + %s' %
              (" or ".join(choice.name for choice in type_.choices),
              self._util_cc_helper.GetValueTypeString('value'))))
        .Append('return false;'))
    elif type_.property_type == PropertyType.OBJECT:
      (c.Sblock('if (!value.is_dict()) {')
        .Concat(self._AppendError16(
          'u"expected dictionary, got " + ' +
          self._util_cc_helper.GetValueTypeString('value')))
        .Append('return false;')
        .Eblock('}'))

      if type_.properties or type_.additional_properties is not None:
        c.Append('const auto* dict = '
                     'static_cast<const base::DictionaryValue*>(&value);')

      # TODO(crbug.com/1145154): The generated code here will ignore
      # unrecognized keys, but the parsing code for types passed to APIs in the
      # renderer will hard-error on them. We should probably be consistent with
      # the renderer here (at least for types also parsed in the renderer).
      for prop in type_.properties.values():
        c.Concat(self._InitializePropertyToDefault(prop, 'out'))
      for prop in type_.properties.values():
        c.Concat(self._GenerateTypePopulateProperty(prop, 'dict', 'out'))
      if type_.additional_properties is not None:
        if type_.additional_properties.property_type == PropertyType.ANY:
          c.Append('out->additional_properties.MergeDictionary(dict);')
        else:
          cpp_type = self._type_helper.GetCppType(type_.additional_properties,
                                                  is_in_container=True)
          (c.Append('for (base::DictionaryValue::Iterator it(*dict);')
            .Sblock('     !it.IsAtEnd(); it.Advance()) {')
              .Append('%s tmp;' % cpp_type)
              .Concat(self._GeneratePopulateVariableFromValue(
                  type_.additional_properties,
                  '(&it.value())',
                  'tmp',
                  'false'))
              .Append('out->additional_properties[it.key()] = tmp;')
            .Eblock('}')
          )
      c.Append('return true;')
    (c.Eblock('}')
      .Substitute({'namespace': cpp_namespace, 'name': classname}))
    return c

  def _GenerateValueIsTypeExpression(self, var, type_):
    real_type = self._type_helper.FollowRef(type_)
    if real_type.property_type is PropertyType.CHOICES:
      return '(%s)' % ' || '.join(self._GenerateValueIsTypeExpression(var,
                                                                      choice)
                                  for choice in real_type.choices)
    return '%s.type() == %s' % (var, cpp_util.GetValueType(real_type))

  def _GenerateTypePopulateProperty(self, prop, src, dst):
    """Generate the code to populate a single property in a type.

    src: base::DictionaryValue*
    dst: Type*
    """
    c = Code()
    value_var = prop.unix_name + '_value'
    c.Append('const base::Value* %(value_var)s = %(src)s->FindKey("%(key)s");')
    if prop.optional:
      (c.Sblock(
          'if (%(value_var)s) {')
        .Concat(self._GeneratePopulatePropertyFromValue(
            prop, value_var, dst, 'false')))
      underlying_type = self._type_helper.FollowRef(prop.type_)
      if underlying_type.property_type == PropertyType.ENUM:
        namespace_prefix = ('%s::' % underlying_type.namespace.unix_name
                            if underlying_type.namespace != self._namespace
                            else '')
        (c.Append('} else {')
          .Append('%%(dst)s->%%(name)s = %s%s;' %
             (namespace_prefix,
              self._type_helper.GetEnumNoneValue(prop.type_))))
      c.Eblock('}')
    else:
      (c.Sblock(
          'if (!%(value_var)s) {')
        .Concat(self._AppendError16('u"\'%%(key)s\' is required"'))
        .Append('return false;')
        .Eblock('}')
        .Concat(self._GeneratePopulatePropertyFromValue(
            prop, value_var, dst, 'false'))
      )
    c.Append()
    c.Substitute({
      'value_var': value_var,
      'key': prop.name,
      'src': src,
      'dst': dst,
      'name': prop.unix_name
    })
    return c

  def _GenerateTypeFromValue(self, cpp_namespace, type_):
    classname = cpp_util.Classname(schema_util.StripNamespace(type_.name))
    c = Code()
    (c.Append('// static')
      .Append('std::unique_ptr<%s> %s::FromValue(%s) {' % (classname,
        cpp_namespace, self._GenerateParams(('const base::Value& value',))))
    )
    c.Sblock();
    if self._generate_error_messages:
      c.Append('DCHECK(error);')
    c.Append('auto out = std::make_unique<%s>();' % classname)
    c.Append('bool result = Populate(%s);' %
      self._GenerateArgs(('value', 'out.get()')))
    if self._generate_error_messages:
      c.Append('DCHECK_EQ(result, error->empty());')
    c.Sblock('if (!result)')
    c.Append('return nullptr;')
    c.Eblock('return out;')
    c.Eblock('}')
    return c

  def _GenerateTypeToValue(self, cpp_namespace, type_):
    """Generates a function that serializes the type into a base::Value.
    E.g. for type "Foo" generates Foo::ToValue()
    """
    if type_.property_type == PropertyType.OBJECT:
      return self._GenerateObjectTypeToValue(cpp_namespace, type_)
    elif type_.property_type == PropertyType.CHOICES:
      return self._GenerateChoiceTypeToValue(cpp_namespace, type_)
    else:
      raise ValueError("Unsupported property type %s" % type_.type_)

  def _GenerateManifestKeysIncludes(self):
    # type: () -> (Code)
    """Returns the includes needed for manifest key parsing.
    """
    c = Code()
    if not self._namespace.manifest_keys:
      return c

    c.Append('#include "tools/json_schema_compiler/manifest_parse_util.h"')
    return c

  def _GenerateManifestKeyConstants(self, classname_in_namespace, properties):
    # type: (str, List[Property]) -> Code
    """ Generates the definition for manifest key constants declared in the
    header.
    """
    c = Code()
    for prop in properties:
      c.Comment('static')
      c.Append('constexpr char %s::%s[];' %
               (classname_in_namespace,
                cpp_util.UnixNameToConstantName(prop.unix_name)))

    return c

  def _GenerateManifestKeys(self):
    # type: () -> Code
    """Generates the types and parsing code for manifest keys.
    """
    assert self._namespace.manifest_keys
    assert self._namespace.manifest_keys.property_type == PropertyType.OBJECT
    return self._GenerateType(None, self._namespace.manifest_keys)

  def _GenerateParseFromDictionary(
    self, classname, classname_in_namespace, type_):
    # type: (str, str, Type) -> Code
    """Generates a function that deserializes the type from the passed
    dictionary. E.g. for type "Foo", generates Foo::ParseFromDictionary().
    """
    assert type_.property_type == PropertyType.OBJECT, \
      ('Manifest type %s must be an object, but it is: %s' %
      (type_.name, type_.property_type))

    if type_.IsRootManifestKeyType():
      return self._GenerateParseFromDictionaryForRootManifestType(
        classname, classname_in_namespace, type_.properties.values())
    return self._GenerateParseFromDictionaryForChildManifestType(
      classname, classname_in_namespace, type_.properties.values())

  def _GenerateParseFromDictionaryForRootManifestType(
    self, classname, classname_in_namespace, properties):
    # type: (str, str, List[Property]) -> Code
    """Generates definition for ManifestKeys::ParseFromDictionary.
    """
    params = [
      'const base::DictionaryValue& root_dict',
      '%(classname)s* out'
    ]

    c = Code()
    c.Append('//static')
    c.Append('bool %(classname_in_namespace)s::ParseFromDictionary(')

    # Make |generate_error_messages| True since we always generate error
    # messages for manifest parsing.
    c.Sblock('%s) {' %
             self._GenerateParams(params, generate_error_messages=True))

    c.Append('DCHECK(out);')
    c.Append('DCHECK(error);')
    c.Append()

    c.Append('std::vector<base::StringPiece> error_path_reversed_vec;')
    c.Append('auto* error_path_reversed = &error_path_reversed_vec;')
    c.Append('const base::DictionaryValue& dict = root_dict;')

    for prop in properties:
      c.Concat(self._InitializePropertyToDefault(prop, 'out'))

    for prop in properties:
      c.Cblock(
        self._ParsePropertyFromDictionary(prop, is_root_manifest_type=True))

    c.Append('return true;')
    c.Eblock('}')
    c.Substitute({
      'classname_in_namespace': classname_in_namespace,
      'classname': classname
    })
    return c

  def _GenerateParseFromDictionaryForChildManifestType(
    self, classname, classname_in_namespace, properties):
    # type: (str, str, List[Property]) -> Code
    """Generates T::ParseFromDictionary for a child manifest type.
    """
    params = [
      'const base::DictionaryValue& root_dict',
      'base::StringPiece key',
      '%(classname)s* out',
      'std::u16string* error',
      'std::vector<base::StringPiece>* error_path_reversed'
    ]

    c = Code()
    c.Append('//static')
    c.Append('bool %(classname_in_namespace)s::ParseFromDictionary(')

    # Make |generate_error_messages| False since |error| is already included
    # within |params|.
    c.Sblock('%s) {' %
             self._GenerateParams(params, generate_error_messages=False))

    c.Append('DCHECK(out);')
    c.Append('DCHECK(error);')
    c.Append('DCHECK(error_path_reversed);')
    c.Append()

    c.Append(
      'const base::Value* value = '
      '::json_schema_compiler::manifest_parse_util::FindKeyOfType('
      'root_dict, key, base::Value::Type::DICTIONARY, error, '
      'error_path_reversed);'
    )
    c.Sblock('if (!value)')
    c.Append('return false;')
    c.Eblock('const base::DictionaryValue& dict = '
             'base::Value::AsDictionaryValue(*value);')

    for prop in properties:
      c.Concat(self._InitializePropertyToDefault(prop, 'out'))

    for prop in properties:
      c.Cblock(
        self._ParsePropertyFromDictionary(prop, is_root_manifest_type=False))

    c.Append('return true;')
    c.Eblock('}')
    c.Substitute({
      'classname_in_namespace': classname_in_namespace,
      'classname': classname
    })
    return c

  def _ParsePropertyFromDictionary(self, property, is_root_manifest_type):
    # type: (Property, bool) -> Code
    """Generates the code to parse a single property from a dictionary.
    """
    supported_property_types = {
      PropertyType.ARRAY,
      PropertyType.BOOLEAN,
      PropertyType.DOUBLE,
      PropertyType.INT64,
      PropertyType.INTEGER,
      PropertyType.OBJECT,
      PropertyType.STRING,
      PropertyType.ENUM
    }

    c = Code()
    underlying_type = self._type_helper.FollowRef(property.type_)
    underlying_property_type = underlying_type.property_type
    underlying_item_type = (
      self._type_helper.FollowRef(underlying_type.item_type)
      if underlying_property_type is PropertyType.ARRAY
      else None)

    assert (underlying_property_type in supported_property_types), (
      'Property type not implemented for %s, type: %s, namespace: %s' %
      (underlying_property_type, underlying_type.name,
      underlying_type.namespace.name))

    property_constant = cpp_util.UnixNameToConstantName(property.unix_name)
    out_expression = '&out->%s' % property.unix_name

    def get_enum_params(enum_type, include_optional_param):
      # type: (Type, bool) -> List[str]
      enum_name = cpp_util.Classname(
        schema_util.StripNamespace(enum_type.name))
      cpp_type_namespace = (''
        if enum_type.namespace == self._namespace
        else '%s::' % enum_type.namespace.unix_name)

      params = [
        'dict',
        '%s' % property_constant,
        '&%sParse%s' % (cpp_type_namespace, enum_name)
      ]
      if include_optional_param:
        params.append('true' if property.optional else 'false')
      params += [
        '%s%s' % (cpp_type_namespace,
                  self._type_helper.GetEnumNoneValue(enum_type)),
        '%s' % out_expression,
        'error',
        'error_path_reversed'
      ]
      return params

    if underlying_property_type == PropertyType.ENUM:
      params = get_enum_params(underlying_type, include_optional_param=True)
      func_name = 'ParseEnumFromDictionary'
    elif underlying_item_type and \
      underlying_item_type.property_type == PropertyType.ENUM:
      # Array of enums.
      params = get_enum_params(underlying_item_type,
                               include_optional_param=False)
      func_name = 'ParseEnumArrayFromDictionary'
    else:
      params = [
        'dict',
        '%s' % property_constant,
        '%s' % out_expression,
        'error',
        'error_path_reversed'
      ]
      func_name = 'ParseFromDictionary'

    c.Sblock(
      'if (!::json_schema_compiler::manifest_parse_util::%s(%s)) {'
      % (func_name, self._GenerateParams(params, generate_error_messages=False))
    )
    if is_root_manifest_type:
      c.Append('::json_schema_compiler::manifest_parse_util::'
        'PopulateFinalError(error, error_path_reversed);')
    else:
      c.Append('error_path_reversed->push_back(key);')
    c.Append('return false;')
    c.Eblock('}')

    return c

  def _GenerateObjectTypeToValue(self, cpp_namespace, type_):
    """Generates a function that serializes an object-representing type
    into a base::DictionaryValue.
    """
    c = Code()
    (c.Sblock('std::unique_ptr<base::DictionaryValue> %s::ToValue() const {' %
          cpp_namespace)
        .Append('auto to_value_result =')
        .Append('    std::make_unique<base::DictionaryValue>();')
        .Append()
    )

    for prop in type_.properties.values():
      prop_var = 'this->%s' % prop.unix_name
      if prop.optional:
        underlying_type = self._type_helper.FollowRef(prop.type_)
        if underlying_type.property_type == PropertyType.ENUM:
          # Optional enum values are generated with a NONE enum value,
          # potentially from another namespace.
          maybe_namespace = ''
          if underlying_type.namespace != self._namespace:
            maybe_namespace = '%s::' % underlying_type.namespace.unix_name
          c.Sblock('if (%s != %s%s) {' %
              (prop_var,
               maybe_namespace,
               self._type_helper.GetEnumNoneValue(prop.type_)))
        else:
          c.Sblock('if (%s.get()) {' % prop_var)

      # ANY is a base::Value which is abstract and cannot be a direct member, so
      # it will always be a pointer.
      is_ptr = prop.optional or prop.type_.property_type == PropertyType.ANY
      c.Cblock(self._CreateValueFromType(
          'to_value_result->SetWithoutPathExpansion("%s", %%s);' % prop.name,
          prop.name,
          prop.type_,
          prop_var,
          is_ptr=is_ptr))

      if prop.optional:
        c.Eblock('}')

    if type_.additional_properties is not None:
      if type_.additional_properties.property_type == PropertyType.ANY:
        c.Append('to_value_result->MergeDictionary(&additional_properties);')
      else:
        (c.Sblock('for (const auto& it : additional_properties) {')
          .Cblock(self._CreateValueFromType(
              'to_value_result->SetWithoutPathExpansion(it.first, %s);',
              type_.additional_properties.name,
              type_.additional_properties,
              'it.second'))
          .Eblock('}')
        )

    return (c.Append()
             .Append('return to_value_result;')
           .Eblock('}'))

  def _GenerateChoiceTypeToValue(self, cpp_namespace, type_):
    """Generates a function that serializes a choice-representing type
    into a base::Value.
    """
    c = Code()
    c.Sblock('std::unique_ptr<base::Value> %s::ToValue() const {' %
                 cpp_namespace)
    c.Append('std::unique_ptr<base::Value> result;')
    for choice in type_.choices:
      choice_var = 'as_%s' % choice.unix_name
      # Enums cannot be wrapped with scoped_ptr, but the XXX_NONE enum value
      # is equal to 0.
      (c.Sblock('if (%s) {' % choice_var)
       .Append('DCHECK(!result) << "Cannot set multiple choices for %s";' %
               type_.unix_name).Cblock(self._CreateValueFromType(
                   'result = %s;', choice.name, choice, choice_var, True))
       .Eblock('}'))
    (c.Append('DCHECK(result) << "Must set at least one choice for %s";' %
              type_.unix_name).Append('return result;').Eblock('}'))
    return c

  def _GenerateFunction(self, function):
    """Generates the definitions for function structs.
    """
    c = Code()

    # TODO(kalman): use function.unix_name not Classname.
    function_namespace = cpp_util.Classname(function.name)
    # Windows has a #define for SendMessage, so to avoid any issues, we need
    # to not use the name.
    if function_namespace == 'SendMessage':
      function_namespace = 'PassMessage'
    (c.Append('namespace %s {' % function_namespace)
      .Append()
    )

    # Params::Populate function
    if function.params:
      c.Concat(self._GeneratePropertyFunctions('Params', function.params))
      (c.Append('Params::Params() = default;')
        .Append('Params::~Params() = default;')
        .Append()
        .Cblock(self._GenerateFunctionParamsCreate(function))
      )

    # Results::Create function
    if function.returns_async:
      c.Concat(
          self._GenerateAsyncResponseArguments('Results',
                                              function.returns_async.params))

    c.Append('}  // namespace %s' % function_namespace)
    return c

  def _GenerateEvent(self, event):
    # TODO(kalman): use event.unix_name not Classname.
    c = Code()
    event_namespace = cpp_util.Classname(event.name)
    (c.Append('namespace %s {' % event_namespace)
      .Append()
      .Cblock(self._GenerateEventNameConstant(event))
      .Cblock(self._GenerateAsyncResponseArguments(None, event.params))
      .Append('}  // namespace %s' % event_namespace)
    )
    return c

  def _CreateValueFromType(self, code, prop_name, type_, var, is_ptr=False):
    """Creates a base::Value given a type. Generated code passes ownership
    to caller via std::unique_ptr.

    var: variable or variable*

    E.g for std::string, generate new base::Value(var)
    """
    c = Code()
    underlying_type = self._type_helper.FollowRef(type_)
    if underlying_type.property_type == PropertyType.ARRAY:
      # Enums are treated specially because C++ templating thinks that they're
      # ints, but really they're strings. So we create a vector of strings and
      # populate it with the names of the enum in the array. The |ToString|
      # function of the enum can be in another namespace when the enum is
      # referenced. Templates can not be used here because C++ templating does
      # not support passing a namespace as an argument.
      item_type = self._type_helper.FollowRef(underlying_type.item_type)
      if item_type.property_type == PropertyType.ENUM:
        varname = ('*' if is_ptr else '') + '(%s)' % var

        maybe_namespace = ''
        if type_.item_type.property_type == PropertyType.REF:
          maybe_namespace = '%s::' % item_type.namespace.unix_name

        enum_list_var = '%s_list' % prop_name
        # Scope the std::vector variable declaration inside braces.
        (c.Sblock('{')
          .Append('std::vector<std::string> %s;' % enum_list_var)
          .Append('for (const auto& it : %s) {' % varname)
          .Append('%s.push_back(%sToString(it));' % (enum_list_var,
                                                     maybe_namespace))
          .Eblock('}'))

        # Because the std::vector above is always created for both required and
        # optional enum arrays, |is_ptr| is set to false and uses the
        # std::vector to create the values.
        (c.Append(code %
            self._GenerateCreateValueFromType(type_, enum_list_var, False))
          .Append('}'))
        return c

    c.Append(code % self._GenerateCreateValueFromType(type_, var, is_ptr))
    return c

  def _GenerateCreateValueFromType(self, type_, var, is_ptr):
    """Generates the statement to create a base::Value given a type.

    type_:  The type of the values being converted.
    var:    The name of the variable.
    is_ptr: Whether |type_| is optional.
    """
    underlying_type = self._type_helper.FollowRef(type_)
    if (underlying_type.property_type == PropertyType.CHOICES or
        underlying_type.property_type == PropertyType.OBJECT):
      if is_ptr:
        return '(%s)->ToValue()' % var
      else:
        return '(%s).ToValue()' % var
    elif (underlying_type.property_type == PropertyType.ANY or
          (underlying_type.property_type == PropertyType.FUNCTION and
               not underlying_type.is_serializable_function)):
      if is_ptr:
        vardot = '(%s)->' % var
      else:
        vardot = '(%s).' % var
      return '%sCreateDeepCopy()' % vardot
    elif underlying_type.property_type == PropertyType.ENUM:
      maybe_namespace = ''
      if type_.property_type == PropertyType.REF:
        maybe_namespace = '%s::' % underlying_type.namespace.unix_name
      return 'std::make_unique<base::Value>(%sToString(%s))' % (
          maybe_namespace, var)
    elif underlying_type.property_type == PropertyType.BINARY:
      if is_ptr:
        var = '*%s' % var
      return 'std::make_unique<base::Value>(%s)' % var
    elif underlying_type.property_type == PropertyType.ARRAY:
      if is_ptr:
        var = '*%s' % var
      return '%s' % self._util_cc_helper.CreateValueFromArray(var)
    elif (underlying_type.property_type.is_fundamental or
              underlying_type.is_serializable_function):
      if is_ptr:
        var = '*%s' % var
      return 'std::make_unique<base::Value>(%s)' % var
    else:
      raise NotImplementedError('Conversion of %s to base::Value not '
                                'implemented' % repr(type_.type_))

  def _GenerateParamsCheck(self, function, var):
    """Generates a check for the correct number of arguments when creating
    Params.
    """
    c = Code()
    num_required = 0
    for param in function.params:
      if not param.optional:
        num_required += 1
    if num_required == len(function.params):
      c.Sblock('if (%(var)s.GetSize() != %(total)d) {')
    elif not num_required:
      c.Sblock('if (%(var)s.GetSize() > %(total)d) {')
    else:
      c.Sblock('if (%(var)s.GetSize() < %(required)d'
          ' || %(var)s.GetSize() > %(total)d) {')
    (c.Concat(self._AppendError16(
        'u"expected %%(total)d arguments, got " '
        '+ base::NumberToString16(%%(var)s.GetSize())'))
      .Append('return nullptr;')
      .Eblock('}')
      .Substitute({
        'var': var,
        'required': num_required,
        'total': len(function.params),
    }))
    return c

  def _GenerateFunctionParamsCreate(self, function):
    """Generate function to create an instance of Params. The generated
    function takes a base::ListValue of arguments.

    E.g for function "Bar", generate Bar::Params::Create()
    """
    c = Code()
    (c.Append('// static')
      .Sblock('std::unique_ptr<Params> Params::Create(%s) {' %
                  self._GenerateParams(['const base::ListValue& args']))
    )
    if self._generate_error_messages:
      c.Append('DCHECK(error);')
    (c.Concat(self._GenerateParamsCheck(function, 'args'))
      .Append('std::unique_ptr<Params> params(new Params());')
    )

    for param in function.params:
      c.Concat(self._InitializePropertyToDefault(param, 'params'))

    for i, param in enumerate(function.params):
      # Any failure will cause this function to return. If any argument is
      # incorrect or missing, those following it are not processed. Note that
      # for optional arguments, we allow missing arguments and proceed because
      # there may be other arguments following it.
      failure_value = 'std::unique_ptr<Params>()'
      c.Append()
      value_var = param.unix_name + '_value'
      (c.Append('const base::Value* %(value_var)s = nullptr;')
        .Append('if (args.Get(%(i)s, &%(value_var)s) &&')
        .Sblock('    !%(value_var)s->is_none()) {')
        .Concat(self._GeneratePopulatePropertyFromValue(
            param, value_var, 'params', failure_value))
        .Eblock('}')
      )
      if not param.optional:
        (c.Sblock('else {')
          .Concat(self._AppendError16('u"\'%%(key)s\' is required"'))
          .Append('return %s;' % failure_value)
          .Eblock('}'))
      c.Substitute({'value_var': value_var, 'i': i, 'key': param.name})
    (c.Append()
      .Append('return params;')
      .Eblock('}')
      .Append()
    )

    return c

  def _GeneratePopulatePropertyFromValue(self,
                                         prop,
                                         src_var,
                                         dst_class_var,
                                         failure_value):
    """Generates code to populate property |prop| of |dst_class_var| (a
    pointer) from a Value*. See |_GeneratePopulateVariableFromValue| for
    semantics.
    """
    return self._GeneratePopulateVariableFromValue(prop.type_,
                                                   src_var,
                                                   '%s->%s' % (dst_class_var,
                                                               prop.unix_name),
                                                   failure_value,
                                                   is_ptr=prop.optional)

  def _GeneratePopulateVariableFromValue(self,
                                         type_,
                                         src_var,
                                         dst_var,
                                         failure_value,
                                         is_ptr=False):
    """Generates code to populate a variable |dst_var| of type |type_| from a
    Value* at |src_var|. The Value* is assumed to be non-null. In the generated
    code, if |dst_var| fails to be populated then Populate will return
    |failure_value|.
    """
    c = Code()

    underlying_type = self._type_helper.FollowRef(type_)

    if (underlying_type.property_type.is_fundamental or
        underlying_type.is_serializable_function):
      is_string_or_function = (
        underlying_type.property_type == PropertyType.STRING
        or (underlying_type.property_type == PropertyType.FUNCTION
          and underlying_type.is_serializable_function))
      c.Append('auto%s temp = %s;' % (
        '*' if is_string_or_function else '',
        cpp_util.GetAsFundamentalValue(underlying_type, src_var)
      ))
      if is_string_or_function:
        (c.Sblock('if (!temp) {')
          .Concat(self._AppendError16(
            'u"\'%%(key)s\': expected ' + '%s, got " + %s' % (
                type_.name,
                self._util_cc_helper.GetValueTypeString(
                    '%%(src_var)s', True)))))
      else:
        (c.Sblock('if (!temp.has_value()) {')
          .Concat(self._AppendError16(
            'u"\'%%(key)s\': expected ' + '%s, got " + %s' % (
                type_.name,
                self._util_cc_helper.GetValueTypeString(
                    '%%(src_var)s', True)))))
      if is_ptr:
        c.Append('%(dst_var)s.reset();')
      c.Append('return %(failure_value)s;')
      (c.Eblock('}'))
      if is_ptr:
        if is_string_or_function:
          c.Append('%(dst_var)s = std::make_unique<%(cpp_type)s>(*temp);')
        else:
          c.Append('%(dst_var)s = ' +
            'std::make_unique<%(cpp_type)s>(temp.value());')
      else:
        if is_string_or_function:
          c.Append('%(dst_var)s = *temp;')
        else:
          c.Append('%(dst_var)s = temp.value();')
    elif underlying_type.property_type == PropertyType.OBJECT:
      if is_ptr:
        (c.Append('const base::DictionaryValue* dictionary = nullptr;')
          .Sblock('if (!%(src_var)s->GetAsDictionary(&dictionary)) {')
          .Concat(self._AppendError16(
            'u"\'%%(key)s\': expected dictionary, got " + ' +
            self._util_cc_helper.GetValueTypeString('%%(src_var)s', True)))
          .Append('return %(failure_value)s;')
        )
        (c.Eblock('}')
          .Sblock('else {')
          .Append('auto temp = std::make_unique<%(cpp_type)s>();')
          .Append('if (!%%(cpp_type)s::Populate(%s)) {' % self._GenerateArgs(
            ('*dictionary', 'temp.get()')))
          .Append('  return %(failure_value)s;')
        )
        (c.Append('}')
          .Append('else')
         .Append('  %(dst_var)s = std::move(temp);')
          .Eblock('}')
        )
      else:
        (c.Append('const base::DictionaryValue* dictionary = nullptr;')
          .Sblock('if (!%(src_var)s->GetAsDictionary(&dictionary)) {')
          .Concat(self._AppendError16(
            'u"\'%%(key)s\': expected dictionary, got " + ' +
            self._util_cc_helper.GetValueTypeString('%%(src_var)s', True)))
          .Append('return %(failure_value)s;')
          .Eblock('}')
          .Append('if (!%%(cpp_type)s::Populate(%s)) {' % self._GenerateArgs(
            ('*dictionary', '&%(dst_var)s')))
          .Append('  return %(failure_value)s;')
          .Append('}')
        )
    elif underlying_type.property_type == PropertyType.FUNCTION:
      assert not underlying_type.is_serializable_function, \
          'Serializable functions should have been handled above.'
      if is_ptr: # Non-serializable functions are just represented as dicts.
        c.Append('%(dst_var)s = std::make_unique<base::DictionaryValue>();')
    elif underlying_type.property_type == PropertyType.ANY:
      c.Append('%(dst_var)s = %(src_var)s->CreateDeepCopy();')
    elif underlying_type.property_type == PropertyType.ARRAY:
      # util_cc_helper deals with optional and required arrays
      (c.Append('const base::ListValue* list = nullptr;')
        .Sblock('if (!%(src_var)s->GetAsList(&list)) {')
        .Concat(self._AppendError16(
          'u"\'%%(key)s\': expected list, got " + ' +
          self._util_cc_helper.GetValueTypeString('%%(src_var)s', True)))
        .Append('return %(failure_value)s;')
      )
      c.Eblock('}')
      c.Sblock('else {')
      item_type = self._type_helper.FollowRef(underlying_type.item_type)
      if item_type.property_type == PropertyType.ENUM:
        c.Concat(self._GenerateListValueToEnumArrayConversion(
                     item_type,
                     'list',
                     dst_var,
                     failure_value,
                     is_ptr=is_ptr))
      else:
        args = ['*list', '&%(dst_var)s']
        if self._generate_error_messages:
          c.Append('std::u16string array_parse_error;')
          args.append('&array_parse_error')

        c.Append('if (!%s(%s)) {' % (
            self._util_cc_helper.PopulateArrayFromListFunction(is_ptr),
            self._GenerateArgs(args, generate_error_messages=False)))
        c.Sblock()
        if self._generate_error_messages:
          c.Append(
            'array_parse_error = u"Error at key \'%(key)s\': " + '
            'array_parse_error;'
          )
          c.Concat(self._AppendError16('array_parse_error'))
        c.Append('return %(failure_value)s;')
        c.Eblock('}')
      c.Eblock('}')
    elif underlying_type.property_type == PropertyType.CHOICES:
      if is_ptr:
        (c.Append('auto temp = std::make_unique<%(cpp_type)s>();')
          .Append('if (!%%(cpp_type)s::Populate(%s))' % self._GenerateArgs(
            ('*%(src_var)s', 'temp.get()')))
          .Append('  return %(failure_value)s;')
          .Append('%(dst_var)s = std::move(temp);')
        )
      else:
        (c.Append('if (!%%(cpp_type)s::Populate(%s))' % self._GenerateArgs(
            ('*%(src_var)s', '&%(dst_var)s')))
          .Append('  return %(failure_value)s;'))
    elif underlying_type.property_type == PropertyType.ENUM:
      c.Concat(self._GenerateStringToEnumConversion(underlying_type,
                                                    src_var,
                                                    dst_var,
                                                    failure_value))
    elif underlying_type.property_type == PropertyType.BINARY:
      (c.Sblock('if (!%(src_var)s->is_blob()) {')
        .Concat(self._AppendError16(
          'u"\'%%(key)s\': expected binary, got " + ' +
          self._util_cc_helper.GetValueTypeString('%%(src_var)s', True)))
        .Append('return %(failure_value)s;')
      )
      (c.Eblock('}')
        .Sblock('else {')
      )
      if is_ptr:
        c.Append('%(dst_var)s = std::make_unique<std::vector<uint8_t>>('
                 '%(src_var)s->GetBlob());')
      else:
        c.Append('%(dst_var)s = %(src_var)s->GetBlob();')
      c.Eblock('}')
    else:
      raise NotImplementedError(type_)
    if c.IsEmpty():
      return c
    return Code().Sblock('{').Concat(c.Substitute({
      'cpp_type': self._type_helper.GetCppType(type_),
      'src_var': src_var,
      'dst_var': dst_var,
      'failure_value': failure_value,
      'key': type_.name,
      'parent_key': type_.parent.name,
    })).Eblock('}')

  def _GenerateListValueToEnumArrayConversion(self,
                                              item_type,
                                              src_var,
                                              dst_var,
                                              failure_value,
                                              is_ptr=False):
    """Returns Code that converts a ListValue of string constants from
    |src_var| into an array of enums of |type_| in |dst_var|. On failure,
    returns |failure_value|.
    """
    c = Code()
    accessor = '.'
    if is_ptr:
      accessor = '->'
      cpp_type = self._type_helper.GetCppType(item_type, is_in_container=True)
      c.Append('%s = std::make_unique<std::vector<%s>>();' %
                   (dst_var, cpp_type))
    (c.Sblock('for (const auto& it : (%s)->GetList()) {' % src_var)
      .Append('%s tmp;' % self._type_helper.GetCppType(item_type))
      .Concat(self._GenerateStringToEnumConversion(item_type,
                                                   '(it)',
                                                   'tmp',
                                                   failure_value,
                                                   is_ptr=False))
      .Append('%s%spush_back(tmp);' % (dst_var, accessor))
      .Eblock('}')
    )
    return c

  def _GenerateStringToEnumConversion(self,
                                      type_,
                                      src_var,
                                      dst_var,
                                      failure_value,
                                      is_ptr=True):
    """Returns Code that converts a string type in |src_var| to an enum with
    type |type_| in |dst_var|. In the generated code, if |src_var| is not
    a valid enum name then the function will return |failure_value|.
    """
    if type_.property_type != PropertyType.ENUM:
      raise TypeError(type_)
    c = Code()
    enum_as_string = '%s_as_string' % type_.unix_name
    cpp_type_namespace = ''
    if type_.namespace != self._namespace:
      cpp_type_namespace = '%s::' % type_.namespace.unix_name
    accessor = '->' if is_ptr else '.'
    (c.Append('std::string %s;' % enum_as_string)
      .Sblock('if (!%s%sGetAsString(&%s)) {' % (src_var,
                                                accessor,
                                                enum_as_string))
      .Concat(self._AppendError16(
        'u"\'%%(key)s\': expected string, got " + ' +
        self._util_cc_helper.GetValueTypeString('%%(src_var)s', is_ptr)))
      .Append('return %s;' % failure_value)
      .Eblock('}')
      .Append('%s = %sParse%s(%s);' % (dst_var,
                                       cpp_type_namespace,
                                       cpp_util.Classname(type_.name),
                                       enum_as_string))
      .Sblock('if (%s == %s%s) {' % (dst_var,
                                     cpp_type_namespace,
                                     self._type_helper.GetEnumNoneValue(type_)))
      .Concat(self._AppendError16(
        'u\"\'%%(key)s\': expected \\"' +
        '\\" or \\"'.join(
            enum_value.name
            for enum_value in self._type_helper.FollowRef(type_).enum_values) +
        '\\", got \\"" + UTF8ToUTF16(%s) + u"\\""' % enum_as_string))
      .Append('return %s;' % failure_value)
      .Eblock('}')
      .Substitute({'src_var': src_var, 'key': type_.name})
    )
    return c

  def _GeneratePropertyFunctions(self, namespace, params):
    """Generates the member functions for a list of parameters.
    """
    return self._GenerateTypes(namespace, (param.type_ for param in params))

  def _GenerateTypes(self, namespace, types):
    """Generates the member functions for a list of types.
    """
    c = Code()
    for type_ in types:
      c.Cblock(self._GenerateType(namespace, type_))
    return c

  def _GenerateEnumToString(self, cpp_namespace, type_):
    """Generates ToString() which gets the string representation of an enum.
    """
    c = Code()
    classname = cpp_util.Classname(schema_util.StripNamespace(type_.name))

    if cpp_namespace is not None:
      c.Append('// static')
    maybe_namespace = '' if cpp_namespace is None else '%s::' % cpp_namespace

    c.Sblock('const char* %sToString(%s enum_param) {' %
                 (maybe_namespace, classname))
    c.Sblock('switch (enum_param) {')
    for enum_value in self._type_helper.FollowRef(type_).enum_values:
      name = enum_value.name
      (c.Append('case %s: ' % self._type_helper.GetEnumValue(type_, enum_value))
        .Append('  return "%s";' % name))
    (c.Append('case %s:' % self._type_helper.GetEnumNoneValue(type_))
      .Append('  return "";')
      .Eblock('}')
      .Append('NOTREACHED();')
      .Append('return "";')
      .Eblock('}')
    )
    return c

  def _GenerateEnumFromString(self, cpp_namespace, type_):
    """Generates FromClassNameString() which gets an enum from its string
    representation.
    """
    c = Code()
    classname = cpp_util.Classname(schema_util.StripNamespace(type_.name))

    if cpp_namespace is not None:
      c.Append('// static')
    maybe_namespace = '' if cpp_namespace is None else '%s::' % cpp_namespace

    c.Sblock('%s%s %sParse%s(const std::string& enum_string) {' %
                 (maybe_namespace, classname, maybe_namespace, classname))
    for _, enum_value in enumerate(
          self._type_helper.FollowRef(type_).enum_values):
      # This is broken up into all ifs with no else ifs because we get
      # "fatal error C1061: compiler limit : blocks nested too deeply"
      # on Windows.
      name = enum_value.name
      (c.Append('if (enum_string == "%s")' % name)
        .Append('  return %s;' %
            self._type_helper.GetEnumValue(type_, enum_value)))
    (c.Append('return %s;' % self._type_helper.GetEnumNoneValue(type_))
      .Eblock('}')
    )
    return c

  def _GenerateAsyncResponseArguments(self, function_scope, params):
    """Generate the function that creates base::Value parameters to return to a
    callback, promise or pass to an event listener.

    E.g for function "Bar", generate Bar::Results::Create
    E.g for event "Baz", generate Baz::Create

    function_scope: the function scope path, e.g. Foo::Bar for the function
                    Foo::Bar::Baz(). May be None if there is no function scope.
    params: the parameters passed as results or event details.
    """
    c = Code()
    c.Concat(self._GeneratePropertyFunctions(function_scope, params))

    (c.Sblock('std::vector<base::Value> %(function_scope)s'
                  'Create(%(declaration_list)s) {')
      .Append('std::vector<base::Value> create_results;')
      .Append('create_results.reserve(%d);' % len(params) if len(params)
              else '')
    )
    declaration_list = []
    for param in params:
      declaration_list.append(cpp_util.GetParameterDeclaration(
          param, self._type_helper.GetCppType(param.type_)))
      c.Cblock(self._CreateValueFromType(
          'create_results.push_back(base::Value::FromUniquePtrValue(%s));',
          param.name,
          param.type_,
          param.unix_name))
    c.Append('return create_results;')
    c.Eblock('}')
    c.Substitute({
        'function_scope': ('%s::' % function_scope) if function_scope else '',
        'declaration_list': ', '.join(declaration_list),
        'param_names': ', '.join(param.unix_name for param in params)
    })
    return c

  def _GenerateEventNameConstant(self, event):
    """Generates a constant string array for the event name.
    """
    c = Code()
    c.Append('const char kEventName[] = "%s.%s";' % (
                 self._namespace.name, event.name))
    return c

  def _InitializePropertyToDefault(self, prop, dst):
    """Initialize a model.Property to its default value inside an object.

    E.g for optional enum "state", generate dst->state = STATE_NONE;

    dst: Type*
    """
    c = Code()
    underlying_type = self._type_helper.FollowRef(prop.type_)
    if (underlying_type.property_type == PropertyType.ENUM and
        prop.optional):
      namespace_prefix = ('%s::' % underlying_type.namespace.unix_name
                          if underlying_type.namespace != self._namespace
                          else '')
      c.Append('%s->%s = %s%s;' % (
        dst,
        prop.unix_name,
        namespace_prefix,
        self._type_helper.GetEnumNoneValue(prop.type_)))
    return c

  def _AppendError16(self, error16):
    """Appends the given |error16| expression/variable to |error|.
    """
    c = Code()
    if not self._generate_error_messages:
      return c
    c.Append('DCHECK(error->empty());')
    c.Append('*error = %s;' % error16)
    return c

  def _GenerateParams(self, params, generate_error_messages=None):
    """Builds the parameter list for a function, given an array of parameters.
    If |generate_error_messages| is specified, it overrides
    |self._generate_error_messages|.
    """
    if generate_error_messages is None:
      generate_error_messages = self._generate_error_messages
    if generate_error_messages:
      params = list(params) + ['std::u16string* error']
    return ', '.join(str(p) for p in params)

  def _GenerateArgs(self, args, generate_error_messages=None):
    """Builds the argument list for a function, given an array of arguments.
    If |generate_error_messages| is specified, it overrides
    |self._generate_error_messages|.
    """
    if generate_error_messages is None:
      generate_error_messages = self._generate_error_messages
    if generate_error_messages:
      args = list(args) + ['error']
    return ', '.join(str(a) for a in args)
