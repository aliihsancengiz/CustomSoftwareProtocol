# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simplestm32.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='simplestm32.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11simplestm32.proto\"0\n\ncomMessage\x12\x10\n\x08pot_val1\x18\x01 \x02(\r\x12\x10\n\x08pot_val2\x18\x02 \x02(\r'
)




_COMMESSAGE = _descriptor.Descriptor(
  name='comMessage',
  full_name='comMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pot_val1', full_name='comMessage.pot_val1', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pot_val2', full_name='comMessage.pot_val2', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['comMessage'] = _COMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

comMessage = _reflection.GeneratedProtocolMessageType('comMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMMESSAGE,
  '__module__' : 'simplestm32_pb2'
  # @@protoc_insertion_point(class_scope:comMessage)
  })
_sym_db.RegisterMessage(comMessage)


# @@protoc_insertion_point(module_scope)
