# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\"b\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\x05genre\x18\x04 \x01(\x0e\x32\x06.Genre\x12\x16\n\x0epublishingYear\x18\x05 \x01(\x05*p\n\x05Genre\x12\x13\n\x0fGENRE_UNDEFINED\x10\x00\x12\x11\n\rGENRE_FANTASY\x10\x01\x12\x1a\n\x16GENRE_SCIENCE_FRICTION\x10\x02\x12\x11\n\rGENRE_MYSTERY\x10\x03\x12\x10\n\x0cGENRE_HORROR\x10\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=114
  _GENRE._serialized_end=226
  _BOOK._serialized_start=14
  _BOOK._serialized_end=112
# @@protoc_insertion_point(module_scope)
