# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_no_generic_services.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/unittest_no_generic_services.proto',
  package='protobuf_unittest.no_generic_services_test',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2google/protobuf/unittest_no_generic_services.proto\x12*protobuf_unittest.no_generic_services_test\"#\n\x0bTestMessage\x12\t\n\x01\x61\x18\x01 \x01(\x05*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02*\x13\n\x08TestEnum\x12\x07\n\x03\x46OO\x10\x01\x32\x86\x01\n\x0bTestService\x12w\n\x03\x46oo\x12\x37.protobuf_unittest.no_generic_services_test.TestMessage\x1a\x37.protobuf_unittest.no_generic_services_test.TestMessage:P\n\x0etest_extension\x12\x37.protobuf_unittest.no_generic_services_test.TestMessage\x18\xe8\x07 \x01(\x05'
)

_TESTENUM = _descriptor.EnumDescriptor(
  name='TestEnum',
  full_name='protobuf_unittest.no_generic_services_test.TestEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FOO', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=135,
  serialized_end=154,
)
_sym_db.RegisterEnumDescriptor(_TESTENUM)

TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
FOO = 1

TEST_EXTENSION_FIELD_NUMBER = 1000
test_extension = _descriptor.FieldDescriptor(
  name='test_extension', full_name='protobuf_unittest.no_generic_services_test.test_extension', index=0,
  number=1000, type=5, cpp_type=1, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='protobuf_unittest.no_generic_services_test.TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='protobuf_unittest.no_generic_services_test.TestMessage.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000, 536870912), ],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.enum_types_by_name['TestEnum'] = _TESTENUM
DESCRIPTOR.extensions_by_name['test_extension'] = test_extension
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), {
  'DESCRIPTOR' : _TESTMESSAGE,
  '__module__' : 'google.protobuf.unittest_no_generic_services_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.no_generic_services_test.TestMessage)
  })
_sym_db.RegisterMessage(TestMessage)

TestMessage.RegisterExtension(test_extension)


_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='protobuf_unittest.no_generic_services_test.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=157,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='Foo',
    full_name='protobuf_unittest.no_generic_services_test.TestService.Foo',
    index=0,
    containing_service=None,
    input_type=_TESTMESSAGE,
    output_type=_TESTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
