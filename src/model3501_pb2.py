# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: model3501.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmodel3501.proto\x12\x08hi_hello\"\x19\n\tHiRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHiResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\",\n\x14\x46indUsbDeviceRequest\x12\x14\n\x0clist_devices\x18\x01 \x01(\x08\"L\n\tUsbDevice\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\x0f\n\x07product\x18\x02 \x01(\t\x12\x18\n\x10\x66irmware_version\x18\x03 \x01(\r\"=\n\x15\x46indUsbDeviceResponse\x12$\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x13.hi_hello.UsbDevice\"\"\n\x0cSpeedRequest\x12\x12\n\nspeed_type\x18\x01 \x01(\t\" \n\rSpeedResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0b\x44\x61taRequest\x12\r\n\x05watts\x18\x01 \x01(\x05\"\x1f\n\x0c\x44\x61taResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x11\n\x0f\x43\x64StressRequest\"#\n\x10\x43\x64StressResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x14\n\x12\x43\x64StressOffRequest\"&\n\x13\x43\x64StressOffResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\rPRswapRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"!\n\x0ePRswapResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\rDRswapRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"!\n\x0e\x44RswapResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x15PdCaptiveCableRequest\")\n\x16PdCaptiveCableResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x16\n\x14PdChargerPortRequest\"(\n\x15PdChargerPortResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb0\x06\n\x0fGreetingService\x12\x34\n\x05SayHi\x12\x13.hi_hello.HiRequest\x1a\x14.hi_hello.HiResponse\"\x00\x12=\n\x08SayHello\x12\x16.hi_hello.HelloRequest\x1a\x17.hi_hello.HelloResponse\"\x00\x12R\n\rFindUsbDevice\x12\x1e.hi_hello.FindUsbDeviceRequest\x1a\x1f.hi_hello.FindUsbDeviceResponse\"\x00\x12\x43\n\x0eSetDeviceSpeed\x12\x16.hi_hello.SpeedRequest\x1a\x17.hi_hello.SpeedResponse\"\x00\x12;\n\x08SendData\x12\x15.hi_hello.DataRequest\x1a\x16.hi_hello.DataResponse\"\x00\x12\x45\n\nCdStressOn\x12\x19.hi_hello.CdStressRequest\x1a\x1a.hi_hello.CdStressResponse\"\x00\x12L\n\x0b\x43\x64StressOff\x12\x1c.hi_hello.CdStressOffRequest\x1a\x1d.hi_hello.CdStressOffResponse\"\x00\x12H\n\x11SendPRswapCommand\x12\x17.hi_hello.PRswapRequest\x1a\x18.hi_hello.PRswapResponse\"\x00\x12H\n\x11SendDRswapCommand\x12\x17.hi_hello.DRswapRequest\x1a\x18.hi_hello.DRswapResponse\"\x00\x12U\n\x0ePdCaptiveCable\x12\x1f.hi_hello.PdCaptiveCableRequest\x1a .hi_hello.PdCaptiveCableResponse\"\x00\x12R\n\rPdChargerPort\x12\x1e.hi_hello.PdChargerPortRequest\x1a\x1f.hi_hello.PdChargerPortResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'model3501_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HIREQUEST']._serialized_start=29
  _globals['_HIREQUEST']._serialized_end=54
  _globals['_HIRESPONSE']._serialized_start=56
  _globals['_HIRESPONSE']._serialized_end=85
  _globals['_HELLOREQUEST']._serialized_start=87
  _globals['_HELLOREQUEST']._serialized_end=115
  _globals['_HELLORESPONSE']._serialized_start=117
  _globals['_HELLORESPONSE']._serialized_end=149
  _globals['_FINDUSBDEVICEREQUEST']._serialized_start=151
  _globals['_FINDUSBDEVICEREQUEST']._serialized_end=195
  _globals['_USBDEVICE']._serialized_start=197
  _globals['_USBDEVICE']._serialized_end=273
  _globals['_FINDUSBDEVICERESPONSE']._serialized_start=275
  _globals['_FINDUSBDEVICERESPONSE']._serialized_end=336
  _globals['_SPEEDREQUEST']._serialized_start=338
  _globals['_SPEEDREQUEST']._serialized_end=372
  _globals['_SPEEDRESPONSE']._serialized_start=374
  _globals['_SPEEDRESPONSE']._serialized_end=406
  _globals['_DATAREQUEST']._serialized_start=408
  _globals['_DATAREQUEST']._serialized_end=436
  _globals['_DATARESPONSE']._serialized_start=438
  _globals['_DATARESPONSE']._serialized_end=469
  _globals['_CDSTRESSREQUEST']._serialized_start=471
  _globals['_CDSTRESSREQUEST']._serialized_end=488
  _globals['_CDSTRESSRESPONSE']._serialized_start=490
  _globals['_CDSTRESSRESPONSE']._serialized_end=525
  _globals['_CDSTRESSOFFREQUEST']._serialized_start=527
  _globals['_CDSTRESSOFFREQUEST']._serialized_end=547
  _globals['_CDSTRESSOFFRESPONSE']._serialized_start=549
  _globals['_CDSTRESSOFFRESPONSE']._serialized_end=587
  _globals['_PRSWAPREQUEST']._serialized_start=589
  _globals['_PRSWAPREQUEST']._serialized_end=618
  _globals['_PRSWAPRESPONSE']._serialized_start=620
  _globals['_PRSWAPRESPONSE']._serialized_end=653
  _globals['_DRSWAPREQUEST']._serialized_start=655
  _globals['_DRSWAPREQUEST']._serialized_end=684
  _globals['_DRSWAPRESPONSE']._serialized_start=686
  _globals['_DRSWAPRESPONSE']._serialized_end=719
  _globals['_PDCAPTIVECABLEREQUEST']._serialized_start=721
  _globals['_PDCAPTIVECABLEREQUEST']._serialized_end=744
  _globals['_PDCAPTIVECABLERESPONSE']._serialized_start=746
  _globals['_PDCAPTIVECABLERESPONSE']._serialized_end=787
  _globals['_PDCHARGERPORTREQUEST']._serialized_start=789
  _globals['_PDCHARGERPORTREQUEST']._serialized_end=811
  _globals['_PDCHARGERPORTRESPONSE']._serialized_start=813
  _globals['_PDCHARGERPORTRESPONSE']._serialized_end=853
  _globals['_GREETINGSERVICE']._serialized_start=856
  _globals['_GREETINGSERVICE']._serialized_end=1672
# @@protoc_insertion_point(module_scope)
