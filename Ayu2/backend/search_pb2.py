# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csearch.proto\"P\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\" \n\x08Response\x12\x14\n\x05items\x18\x01 \x03(\x0b\x32\x05.Item\"#\n\x13GetInventoryRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2@\n\x0bItemService\x12\x31\n\x0cGetInventory\x12\x14.GetInventoryRequest\x1a\t.Response\"\x00\x62\x06proto3')



_ITEM = DESCRIPTOR.message_types_by_name['Item']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_GETINVENTORYREQUEST = DESCRIPTOR.message_types_by_name['GetInventoryRequest']
Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
  'DESCRIPTOR' : _ITEM,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:Item)
  })
_sym_db.RegisterMessage(Item)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

GetInventoryRequest = _reflection.GeneratedProtocolMessageType('GetInventoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINVENTORYREQUEST,
  '__module__' : 'search_pb2'
  # @@protoc_insertion_point(class_scope:GetInventoryRequest)
  })
_sym_db.RegisterMessage(GetInventoryRequest)

_ITEMSERVICE = DESCRIPTOR.services_by_name['ItemService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ITEM._serialized_start=16
  _ITEM._serialized_end=96
  _RESPONSE._serialized_start=98
  _RESPONSE._serialized_end=130
  _GETINVENTORYREQUEST._serialized_start=132
  _GETINVENTORYREQUEST._serialized_end=167
  _ITEMSERVICE._serialized_start=169
  _ITEMSERVICE._serialized_end=233
# @@protoc_insertion_point(module_scope)
