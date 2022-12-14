# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finventory.proto\"b\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\x12\x16\n\x0epublishingYear\x18\x05 \x01(\x05\"a\n\rInventoryItem\x12\x17\n\x0finventoryNumber\x18\x01 \x01(\x05\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12\x17\n\x06status\x18\x03 \x01(\x0e\x32\x07.StatusB\x07\n\x05items\"\x14\n\x04ISBN\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\"[\n\x12\x42ookResponseStatus\x12\x1f\n\nstatusCode\x18\x01 \x01(\x0e\x32\x0b.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x04\x62ook\x18\x03 \x01(\x0b\x32\x05.Book*p\n\x05Genre\x12\x13\n\x0fGENRE_UNDEFINED\x10\x00\x12\x11\n\rGENRE_FANTASY\x10\x01\x12\x1a\n\x16GENRE_SCIENCE_FRICTION\x10\x02\x12\x11\n\rGENRE_MYSTERY\x10\x03\x12\x10\n\x0cGENRE_HORROR\x10\x04*0\n\x06Status\x12\x14\n\x10STATUS_AVAILABLE\x10\x00\x12\x10\n\x0cSTATUS_TAKEN\x10\x01*5\n\nStatusCode\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=333
  _GENRE._serialized_end=445
  _STATUS._serialized_start=447
  _STATUS._serialized_end=495
  _STATUSCODE._serialized_start=497
  _STATUSCODE._serialized_end=550
  _BOOK._serialized_start=19
  _BOOK._serialized_end=117
  _INVENTORYITEM._serialized_start=119
  _INVENTORYITEM._serialized_end=216
  _ISBN._serialized_start=218
  _ISBN._serialized_end=238
  _BOOKRESPONSESTATUS._serialized_start=240
  _BOOKRESPONSESTATUS._serialized_end=331
# @@protoc_insertion_point(module_scope)
