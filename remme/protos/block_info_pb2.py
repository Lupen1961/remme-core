# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='block_info.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62lock_info.proto\"\x81\x01\n\tBlockInfo\x12\x11\n\tblock_num\x18\x01 \x01(\x04\x12\x19\n\x11previous_block_id\x18\x02 \x01(\t\x12\x19\n\x11signer_public_key\x18\x03 \x01(\t\x12\x18\n\x10header_signature\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\"k\n\x0f\x42lockInfoConfig\x12\x14\n\x0clatest_block\x18\x01 \x01(\x04\x12\x14\n\x0coldest_block\x18\x02 \x01(\x04\x12\x14\n\x0ctarget_count\x18\x03 \x01(\x04\x12\x16\n\x0esync_tolerance\x18\x04 \x01(\x04\x62\x06proto3')
)




_BLOCKINFO = _descriptor.Descriptor(
  name='BlockInfo',
  full_name='BlockInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_num', full_name='BlockInfo.block_num', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_block_id', full_name='BlockInfo.previous_block_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signer_public_key', full_name='BlockInfo.signer_public_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header_signature', full_name='BlockInfo.header_signature', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='BlockInfo.timestamp', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=150,
)


_BLOCKINFOCONFIG = _descriptor.Descriptor(
  name='BlockInfoConfig',
  full_name='BlockInfoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latest_block', full_name='BlockInfoConfig.latest_block', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oldest_block', full_name='BlockInfoConfig.oldest_block', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_count', full_name='BlockInfoConfig.target_count', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_tolerance', full_name='BlockInfoConfig.sync_tolerance', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=259,
)

DESCRIPTOR.message_types_by_name['BlockInfo'] = _BLOCKINFO
DESCRIPTOR.message_types_by_name['BlockInfoConfig'] = _BLOCKINFOCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockInfo = _reflection.GeneratedProtocolMessageType('BlockInfo', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKINFO,
  __module__ = 'block_info_pb2'
  # @@protoc_insertion_point(class_scope:BlockInfo)
  ))
_sym_db.RegisterMessage(BlockInfo)

BlockInfoConfig = _reflection.GeneratedProtocolMessageType('BlockInfoConfig', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKINFOCONFIG,
  __module__ = 'block_info_pb2'
  # @@protoc_insertion_point(class_scope:BlockInfoConfig)
  ))
_sym_db.RegisterMessage(BlockInfoConfig)


# @@protoc_insertion_point(module_scope)
