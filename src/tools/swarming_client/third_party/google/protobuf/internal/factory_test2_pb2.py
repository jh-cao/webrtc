# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/factory_test2.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf.internal import factory_test1_pb2 as google_dot_protobuf_dot_internal_dot_factory__test1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/factory_test2.proto',
  package='google.protobuf.python.internal',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/protobuf/internal/factory_test2.proto\x12\x1fgoogle.protobuf.python.internal\x1a,google/protobuf/internal/factory_test1.proto\"\xd8\x0b\n\x0f\x46\x61\x63tory2Message\x12\x11\n\tmandatory\x18\x01 \x02(\x05\x12\x45\n\x0e\x66\x61\x63tory_2_enum\x18\x02 \x01(\x0e\x32-.google.protobuf.python.internal.Factory2Enum\x12\x62\n\x15nested_factory_2_enum\x18\x03 \x01(\x0e\x32\x43.google.protobuf.python.internal.Factory2Message.NestedFactory2Enum\x12h\n\x18nested_factory_2_message\x18\x04 \x01(\x0b\x32\x46.google.protobuf.python.internal.Factory2Message.NestedFactory2Message\x12K\n\x11\x66\x61\x63tory_1_message\x18\x05 \x01(\x0b\x32\x30.google.protobuf.python.internal.Factory1Message\x12\x45\n\x0e\x66\x61\x63tory_1_enum\x18\x06 \x01(\x0e\x32-.google.protobuf.python.internal.Factory1Enum\x12\x62\n\x15nested_factory_1_enum\x18\x07 \x01(\x0e\x32\x43.google.protobuf.python.internal.Factory1Message.NestedFactory1Enum\x12h\n\x18nested_factory_1_message\x18\x08 \x01(\x0b\x32\x46.google.protobuf.python.internal.Factory1Message.NestedFactory1Message\x12J\n\x10\x63ircular_message\x18\t \x01(\x0b\x32\x30.google.protobuf.python.internal.Factory2Message\x12\x14\n\x0cscalar_value\x18\n \x01(\t\x12\x12\n\nlist_value\x18\x0b \x03(\t\x12I\n\x07grouped\x18\x0c \x03(\n28.google.protobuf.python.internal.Factory2Message.Grouped\x12:\n\x04loop\x18\x0f \x01(\x0b\x32,.google.protobuf.python.internal.LoopMessage\x12\x1e\n\x10int_with_default\x18\x10 \x01(\x05:\x04\x31\x37\x37\x36\x12!\n\x13\x64ouble_with_default\x18\x11 \x01(\x01:\x04\x39.99\x12(\n\x13string_with_default\x18\x12 \x01(\t:\x0bhello world\x12 \n\x11\x62ool_with_default\x18\x13 \x01(\x08:\x05\x66\x61lse\x12[\n\x11\x65num_with_default\x18\x14 \x01(\x0e\x32-.google.protobuf.python.internal.Factory2Enum:\x11\x46\x41\x43TORY_2_VALUE_1\x12&\n\x12\x62ytes_with_default\x18\x15 \x01(\x0c:\na\\373\\000c\x12\x13\n\toneof_int\x18\x16 \x01(\x05H\x00\x12\x16\n\x0coneof_string\x18\x17 \x01(\tH\x00\x1a&\n\x15NestedFactory2Message\x12\r\n\x05value\x18\x01 \x01(\t\x1a)\n\x07Grouped\x12\x0e\n\x06part_1\x18\r \x01(\t\x12\x0e\n\x06part_2\x18\x0e \x01(\t\"P\n\x12NestedFactory2Enum\x12\x1c\n\x18NESTED_FACTORY_2_VALUE_0\x10\x00\x12\x1c\n\x18NESTED_FACTORY_2_VALUE_1\x10\x01\x32I\n\x0eone_more_field\x12\x30.google.protobuf.python.internal.Factory1Message\x18\xe9\x07 \x01(\tB\r\n\x0boneof_field\"M\n\x0bLoopMessage\x12>\n\x04loop\x18\x01 \x01(\x0b\x32\x30.google.protobuf.python.internal.Factory2Message\"D\n\x19MessageWithNestedEnumOnly\"\'\n\nNestedEnum\x12\x19\n\x15NESTED_MESSAGE_ENUM_0\x10\x00\"\'\n\x11MessageWithOption\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\x05:\x02\x10\x01*<\n\x0c\x46\x61\x63tory2Enum\x12\x15\n\x11\x46\x41\x43TORY_2_VALUE_0\x10\x00\x12\x15\n\x11\x46\x41\x43TORY_2_VALUE_1\x10\x01:H\n\ranother_field\x12\x30.google.protobuf.python.internal.Factory1Message\x18\xea\x07 \x01(\t'
  ,
  dependencies=[google_dot_protobuf_dot_internal_dot_factory__test1__pb2.DESCRIPTOR,])

_FACTORY2ENUM = _descriptor.EnumDescriptor(
  name='Factory2Enum',
  full_name='google.protobuf.python.internal.Factory2Enum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FACTORY_2_VALUE_0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FACTORY_2_VALUE_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1816,
  serialized_end=1876,
)
_sym_db.RegisterEnumDescriptor(_FACTORY2ENUM)

Factory2Enum = enum_type_wrapper.EnumTypeWrapper(_FACTORY2ENUM)
FACTORY_2_VALUE_0 = 0
FACTORY_2_VALUE_1 = 1

ANOTHER_FIELD_FIELD_NUMBER = 1002
another_field = _descriptor.FieldDescriptor(
  name='another_field', full_name='google.protobuf.python.internal.another_field', index=0,
  number=1002, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

_FACTORY2MESSAGE_NESTEDFACTORY2ENUM = _descriptor.EnumDescriptor(
  name='NestedFactory2Enum',
  full_name='google.protobuf.python.internal.Factory2Message.NestedFactory2Enum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NESTED_FACTORY_2_VALUE_0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NESTED_FACTORY_2_VALUE_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1454,
  serialized_end=1534,
)
_sym_db.RegisterEnumDescriptor(_FACTORY2MESSAGE_NESTEDFACTORY2ENUM)

_MESSAGEWITHNESTEDENUMONLY_NESTEDENUM = _descriptor.EnumDescriptor(
  name='NestedEnum',
  full_name='google.protobuf.python.internal.MessageWithNestedEnumOnly.NestedEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NESTED_MESSAGE_ENUM_0', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1734,
  serialized_end=1773,
)
_sym_db.RegisterEnumDescriptor(_MESSAGEWITHNESTEDENUMONLY_NESTEDENUM)


_FACTORY2MESSAGE_NESTEDFACTORY2MESSAGE = _descriptor.Descriptor(
  name='NestedFactory2Message',
  full_name='google.protobuf.python.internal.Factory2Message.NestedFactory2Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.python.internal.Factory2Message.NestedFactory2Message.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1371,
  serialized_end=1409,
)

_FACTORY2MESSAGE_GROUPED = _descriptor.Descriptor(
  name='Grouped',
  full_name='google.protobuf.python.internal.Factory2Message.Grouped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='part_1', full_name='google.protobuf.python.internal.Factory2Message.Grouped.part_1', index=0,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='part_2', full_name='google.protobuf.python.internal.Factory2Message.Grouped.part_2', index=1,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1411,
  serialized_end=1452,
)

_FACTORY2MESSAGE = _descriptor.Descriptor(
  name='Factory2Message',
  full_name='google.protobuf.python.internal.Factory2Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mandatory', full_name='google.protobuf.python.internal.Factory2Message.mandatory', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factory_2_enum', full_name='google.protobuf.python.internal.Factory2Message.factory_2_enum', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_factory_2_enum', full_name='google.protobuf.python.internal.Factory2Message.nested_factory_2_enum', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_factory_2_message', full_name='google.protobuf.python.internal.Factory2Message.nested_factory_2_message', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factory_1_message', full_name='google.protobuf.python.internal.Factory2Message.factory_1_message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factory_1_enum', full_name='google.protobuf.python.internal.Factory2Message.factory_1_enum', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_factory_1_enum', full_name='google.protobuf.python.internal.Factory2Message.nested_factory_1_enum', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_factory_1_message', full_name='google.protobuf.python.internal.Factory2Message.nested_factory_1_message', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='circular_message', full_name='google.protobuf.python.internal.Factory2Message.circular_message', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scalar_value', full_name='google.protobuf.python.internal.Factory2Message.scalar_value', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_value', full_name='google.protobuf.python.internal.Factory2Message.list_value', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grouped', full_name='google.protobuf.python.internal.Factory2Message.grouped', index=11,
      number=12, type=10, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loop', full_name='google.protobuf.python.internal.Factory2Message.loop', index=12,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_with_default', full_name='google.protobuf.python.internal.Factory2Message.int_with_default', index=13,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1776,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_with_default', full_name='google.protobuf.python.internal.Factory2Message.double_with_default', index=14,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(9.99),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_with_default', full_name='google.protobuf.python.internal.Factory2Message.string_with_default', index=15,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"hello world".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_with_default', full_name='google.protobuf.python.internal.Factory2Message.bool_with_default', index=16,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enum_with_default', full_name='google.protobuf.python.internal.Factory2Message.enum_with_default', index=17,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_with_default', full_name='google.protobuf.python.internal.Factory2Message.bytes_with_default', index=18,
      number=21, type=12, cpp_type=9, label=1,
      has_default_value=True, default_value=b"a\373\000c",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oneof_int', full_name='google.protobuf.python.internal.Factory2Message.oneof_int', index=19,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oneof_string', full_name='google.protobuf.python.internal.Factory2Message.oneof_string', index=20,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='one_more_field', full_name='google.protobuf.python.internal.Factory2Message.one_more_field', index=0,
      number=1001, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_FACTORY2MESSAGE_NESTEDFACTORY2MESSAGE, _FACTORY2MESSAGE_GROUPED, ],
  enum_types=[
    _FACTORY2MESSAGE_NESTEDFACTORY2ENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='oneof_field', full_name='google.protobuf.python.internal.Factory2Message.oneof_field',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=128,
  serialized_end=1624,
)


_LOOPMESSAGE = _descriptor.Descriptor(
  name='LoopMessage',
  full_name='google.protobuf.python.internal.LoopMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='loop', full_name='google.protobuf.python.internal.LoopMessage.loop', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1626,
  serialized_end=1703,
)


_MESSAGEWITHNESTEDENUMONLY = _descriptor.Descriptor(
  name='MessageWithNestedEnumOnly',
  full_name='google.protobuf.python.internal.MessageWithNestedEnumOnly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGEWITHNESTEDENUMONLY_NESTEDENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1705,
  serialized_end=1773,
)


_MESSAGEWITHOPTION = _descriptor.Descriptor(
  name='MessageWithOption',
  full_name='google.protobuf.python.internal.MessageWithOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='google.protobuf.python.internal.MessageWithOption.field1', index=0,
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
  serialized_options=b'\020\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1775,
  serialized_end=1814,
)

_FACTORY2MESSAGE_NESTEDFACTORY2MESSAGE.containing_type = _FACTORY2MESSAGE
_FACTORY2MESSAGE_GROUPED.containing_type = _FACTORY2MESSAGE
_FACTORY2MESSAGE.fields_by_name['factory_2_enum'].enum_type = _FACTORY2ENUM
_FACTORY2MESSAGE.fields_by_name['nested_factory_2_enum'].enum_type = _FACTORY2MESSAGE_NESTEDFACTORY2ENUM
_FACTORY2MESSAGE.fields_by_name['nested_factory_2_message'].message_type = _FACTORY2MESSAGE_NESTEDFACTORY2MESSAGE
_FACTORY2MESSAGE.fields_by_name['factory_1_message'].message_type = google_dot_protobuf_dot_internal_dot_factory__test1__pb2._FACTORY1MESSAGE
_FACTORY2MESSAGE.fields_by_name['factory_1_enum'].enum_type = google_dot_protobuf_dot_internal_dot_factory__test1__pb2._FACTORY1ENUM
_FACTORY2MESSAGE.fields_by_name['nested_factory_1_enum'].enum_type = google_dot_protobuf_dot_internal_dot_factory__test1__pb2._FACTORY1MESSAGE_NESTEDFACTORY1ENUM
_FACTORY2MESSAGE.fields_by_name['nested_factory_1_message'].message_type = google_dot_protobuf_dot_internal_dot_factory__test1__pb2._FACTORY1MESSAGE_NESTEDFACTORY1MESSAGE
_FACTORY2MESSAGE.fields_by_name['circular_message'].message_type = _FACTORY2MESSAGE
_FACTORY2MESSAGE.fields_by_name['grouped'].message_type = _FACTORY2MESSAGE_GROUPED
_FACTORY2MESSAGE.fields_by_name['loop'].message_type = _LOOPMESSAGE
_FACTORY2MESSAGE.fields_by_name['enum_with_default'].enum_type = _FACTORY2ENUM
_FACTORY2MESSAGE_NESTEDFACTORY2ENUM.containing_type = _FACTORY2MESSAGE
_FACTORY2MESSAGE.oneofs_by_name['oneof_field'].fields.append(
  _FACTORY2MESSAGE.fields_by_name['oneof_int'])
_FACTORY2MESSAGE.fields_by_name['oneof_int'].containing_oneof = _FACTORY2MESSAGE.oneofs_by_name['oneof_field']
_FACTORY2MESSAGE.oneofs_by_name['oneof_field'].fields.append(
  _FACTORY2MESSAGE.fields_by_name['oneof_string'])
_FACTORY2MESSAGE.fields_by_name['oneof_string'].containing_oneof = _FACTORY2MESSAGE.oneofs_by_name['oneof_field']
_LOOPMESSAGE.fields_by_name['loop'].message_type = _FACTORY2MESSAGE
_MESSAGEWITHNESTEDENUMONLY_NESTEDENUM.containing_type = _MESSAGEWITHNESTEDENUMONLY
DESCRIPTOR.message_types_by_name['Factory2Message'] = _FACTORY2MESSAGE
DESCRIPTOR.message_types_by_name['LoopMessage'] = _LOOPMESSAGE
DESCRIPTOR.message_types_by_name['MessageWithNestedEnumOnly'] = _MESSAGEWITHNESTEDENUMONLY
DESCRIPTOR.message_types_by_name['MessageWithOption'] = _MESSAGEWITHOPTION
DESCRIPTOR.enum_types_by_name['Factory2Enum'] = _FACTORY2ENUM
DESCRIPTOR.extensions_by_name['another_field'] = another_field
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Factory2Message = _reflection.GeneratedProtocolMessageType('Factory2Message', (_message.Message,), {

  'NestedFactory2Message' : _reflection.GeneratedProtocolMessageType('NestedFactory2Message', (_message.Message,), {
    'DESCRIPTOR' : _FACTORY2MESSAGE_NESTEDFACTORY2MESSAGE,
    '__module__' : 'google.protobuf.internal.factory_test2_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.Factory2Message.NestedFactory2Message)
    })
  ,

  'Grouped' : _reflection.GeneratedProtocolMessageType('Grouped', (_message.Message,), {
    'DESCRIPTOR' : _FACTORY2MESSAGE_GROUPED,
    '__module__' : 'google.protobuf.internal.factory_test2_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.Factory2Message.Grouped)
    })
  ,
  'DESCRIPTOR' : _FACTORY2MESSAGE,
  '__module__' : 'google.protobuf.internal.factory_test2_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.Factory2Message)
  })
_sym_db.RegisterMessage(Factory2Message)
_sym_db.RegisterMessage(Factory2Message.NestedFactory2Message)
_sym_db.RegisterMessage(Factory2Message.Grouped)

LoopMessage = _reflection.GeneratedProtocolMessageType('LoopMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOOPMESSAGE,
  '__module__' : 'google.protobuf.internal.factory_test2_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.LoopMessage)
  })
_sym_db.RegisterMessage(LoopMessage)

MessageWithNestedEnumOnly = _reflection.GeneratedProtocolMessageType('MessageWithNestedEnumOnly', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEWITHNESTEDENUMONLY,
  '__module__' : 'google.protobuf.internal.factory_test2_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.MessageWithNestedEnumOnly)
  })
_sym_db.RegisterMessage(MessageWithNestedEnumOnly)

MessageWithOption = _reflection.GeneratedProtocolMessageType('MessageWithOption', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEWITHOPTION,
  '__module__' : 'google.protobuf.internal.factory_test2_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.MessageWithOption)
  })
_sym_db.RegisterMessage(MessageWithOption)

google_dot_protobuf_dot_internal_dot_factory__test1__pb2.Factory1Message.RegisterExtension(another_field)
google_dot_protobuf_dot_internal_dot_factory__test1__pb2.Factory1Message.RegisterExtension(_FACTORY2MESSAGE.extensions_by_name['one_more_field'])

_MESSAGEWITHOPTION._options = None
# @@protoc_insertion_point(module_scope)
