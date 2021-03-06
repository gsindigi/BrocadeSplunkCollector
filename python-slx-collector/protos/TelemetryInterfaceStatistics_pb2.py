# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TelemetryInterfaceStatistics.proto

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
  name='TelemetryInterfaceStatistics.proto',
  package='telemetry_intf_stats',
  syntax='proto3',
  serialized_pb=_b('\n\"TelemetryInterfaceStatistics.proto\x12\x14telemetry_intf_stats\"\x83\x04\n\rPerfIntfStats\x12\x0e\n\x06ifname\x18\x01 \x01(\t\x12\x10\n\x08if_index\x18\x02 \x01(\x04\x12\x0f\n\x07in_pkts\x18\x03 \x01(\x04\x12\x17\n\x0fin_unicast_pkts\x18\x04 \x01(\x04\x12\x19\n\x11in_broadcast_pkts\x18\x05 \x01(\x04\x12\x19\n\x11in_multicast_pkts\x18\x06 \x01(\x04\x12\x1a\n\x12in_pkts_per_second\x18\x07 \x01(\x04\x12\x14\n\x0cin_bandwidth\x18\x08 \x01(\x04\x12\x11\n\tin_octets\x18\t \x01(\x04\x12\x11\n\tin_errors\x18\n \x01(\x04\x12\x15\n\rin_crc_errors\x18\x0b \x01(\x04\x12\x13\n\x0bin_discards\x18\x0c \x01(\x04\x12\x10\n\x08out_pkts\x18\r \x01(\x04\x12\x18\n\x10out_unicast_pkts\x18\x0e \x01(\x04\x12\x1a\n\x12out_broadcast_pkts\x18\x0f \x01(\x04\x12\x1a\n\x12out_multicast_pkts\x18\x10 \x01(\x04\x12\x1b\n\x13out_pkts_per_second\x18\x11 \x01(\x04\x12\x15\n\rout_bandwidth\x18\x12 \x01(\x04\x12\x12\n\nout_octets\x18\x13 \x01(\x04\x12\x12\n\nout_errors\x18\x14 \x01(\x04\x12\x16\n\x0eout_crc_errors\x18\x15 \x01(\x04\x12\x14\n\x0cout_discards\x18\x16 \x01(\x04\"K\n3BrocadeTelemetryPhysicalInterfaceStatistics_request\x12\x14\n\x0cprofile_name\x18\x01 \x01(\t\"\x90\x01\n4BrocadeTelemetryPhysicalInterfaceStatistics_response\x12\x14\n\x0cprofile_name\x18\x01 \x01(\t\x12\x42\n\x15PerfIntfStats_message\x18\x02 \x03(\x0b\x32#.telemetry_intf_stats.PerfIntfStats2\x80\x02\n3BrocadeTelemetryPhysicalInterfaceStatistics_service\x12\xc8\x01\n+BrocadeTelemetryPhysicalInterfaceStatistics\x12I.telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_request\x1aJ.telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_response\"\x00\x30\x01\x42\x02H\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERFINTFSTATS = _descriptor.Descriptor(
  name='PerfIntfStats',
  full_name='telemetry_intf_stats.PerfIntfStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ifname', full_name='telemetry_intf_stats.PerfIntfStats.ifname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='if_index', full_name='telemetry_intf_stats.PerfIntfStats.if_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_pkts', full_name='telemetry_intf_stats.PerfIntfStats.in_pkts', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_unicast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.in_unicast_pkts', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_broadcast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.in_broadcast_pkts', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_multicast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.in_multicast_pkts', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_pkts_per_second', full_name='telemetry_intf_stats.PerfIntfStats.in_pkts_per_second', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_bandwidth', full_name='telemetry_intf_stats.PerfIntfStats.in_bandwidth', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_octets', full_name='telemetry_intf_stats.PerfIntfStats.in_octets', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_errors', full_name='telemetry_intf_stats.PerfIntfStats.in_errors', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_crc_errors', full_name='telemetry_intf_stats.PerfIntfStats.in_crc_errors', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_discards', full_name='telemetry_intf_stats.PerfIntfStats.in_discards', index=11,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_pkts', full_name='telemetry_intf_stats.PerfIntfStats.out_pkts', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_unicast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.out_unicast_pkts', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_broadcast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.out_broadcast_pkts', index=14,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_multicast_pkts', full_name='telemetry_intf_stats.PerfIntfStats.out_multicast_pkts', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_pkts_per_second', full_name='telemetry_intf_stats.PerfIntfStats.out_pkts_per_second', index=16,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_bandwidth', full_name='telemetry_intf_stats.PerfIntfStats.out_bandwidth', index=17,
      number=18, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_octets', full_name='telemetry_intf_stats.PerfIntfStats.out_octets', index=18,
      number=19, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_errors', full_name='telemetry_intf_stats.PerfIntfStats.out_errors', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_crc_errors', full_name='telemetry_intf_stats.PerfIntfStats.out_crc_errors', index=20,
      number=21, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='out_discards', full_name='telemetry_intf_stats.PerfIntfStats.out_discards', index=21,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=61,
  serialized_end=576,
)


_BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_REQUEST = _descriptor.Descriptor(
  name='BrocadeTelemetryPhysicalInterfaceStatistics_request',
  full_name='telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile_name', full_name='telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_request.profile_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=578,
  serialized_end=653,
)


_BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_RESPONSE = _descriptor.Descriptor(
  name='BrocadeTelemetryPhysicalInterfaceStatistics_response',
  full_name='telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile_name', full_name='telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_response.profile_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PerfIntfStats_message', full_name='telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_response.PerfIntfStats_message', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=656,
  serialized_end=800,
)

_BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_RESPONSE.fields_by_name['PerfIntfStats_message'].message_type = _PERFINTFSTATS
DESCRIPTOR.message_types_by_name['PerfIntfStats'] = _PERFINTFSTATS
DESCRIPTOR.message_types_by_name['BrocadeTelemetryPhysicalInterfaceStatistics_request'] = _BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_REQUEST
DESCRIPTOR.message_types_by_name['BrocadeTelemetryPhysicalInterfaceStatistics_response'] = _BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_RESPONSE

PerfIntfStats = _reflection.GeneratedProtocolMessageType('PerfIntfStats', (_message.Message,), dict(
  DESCRIPTOR = _PERFINTFSTATS,
  __module__ = 'TelemetryInterfaceStatistics_pb2'
  # @@protoc_insertion_point(class_scope:telemetry_intf_stats.PerfIntfStats)
  ))
_sym_db.RegisterMessage(PerfIntfStats)

BrocadeTelemetryPhysicalInterfaceStatistics_request = _reflection.GeneratedProtocolMessageType('BrocadeTelemetryPhysicalInterfaceStatistics_request', (_message.Message,), dict(
  DESCRIPTOR = _BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_REQUEST,
  __module__ = 'TelemetryInterfaceStatistics_pb2'
  # @@protoc_insertion_point(class_scope:telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_request)
  ))
_sym_db.RegisterMessage(BrocadeTelemetryPhysicalInterfaceStatistics_request)

BrocadeTelemetryPhysicalInterfaceStatistics_response = _reflection.GeneratedProtocolMessageType('BrocadeTelemetryPhysicalInterfaceStatistics_response', (_message.Message,), dict(
  DESCRIPTOR = _BROCADETELEMETRYPHYSICALINTERFACESTATISTICS_RESPONSE,
  __module__ = 'TelemetryInterfaceStatistics_pb2'
  # @@protoc_insertion_point(class_scope:telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_response)
  ))
_sym_db.RegisterMessage(BrocadeTelemetryPhysicalInterfaceStatistics_response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\002'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BrocadeTelemetryPhysicalInterfaceStatistics_serviceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.BrocadeTelemetryPhysicalInterfaceStatistics = channel.unary_stream(
        '/telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service/BrocadeTelemetryPhysicalInterfaceStatistics',
        request_serializer=BrocadeTelemetryPhysicalInterfaceStatistics_request.SerializeToString,
        response_deserializer=BrocadeTelemetryPhysicalInterfaceStatistics_response.FromString,
        )


class BrocadeTelemetryPhysicalInterfaceStatistics_serviceServicer(object):

  def BrocadeTelemetryPhysicalInterfaceStatistics(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BrocadeTelemetryPhysicalInterfaceStatistics_serviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'BrocadeTelemetryPhysicalInterfaceStatistics': grpc.unary_stream_rpc_method_handler(
          servicer.BrocadeTelemetryPhysicalInterfaceStatistics,
          request_deserializer=BrocadeTelemetryPhysicalInterfaceStatistics_request.FromString,
          response_serializer=BrocadeTelemetryPhysicalInterfaceStatistics_response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaBrocadeTelemetryPhysicalInterfaceStatistics_serviceServicer(object):
  def BrocadeTelemetryPhysicalInterfaceStatistics(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaBrocadeTelemetryPhysicalInterfaceStatistics_serviceStub(object):
  def BrocadeTelemetryPhysicalInterfaceStatistics(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_BrocadeTelemetryPhysicalInterfaceStatistics_service_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', 'BrocadeTelemetryPhysicalInterfaceStatistics'): BrocadeTelemetryPhysicalInterfaceStatistics_request.FromString,
  }
  response_serializers = {
    ('telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', 'BrocadeTelemetryPhysicalInterfaceStatistics'): BrocadeTelemetryPhysicalInterfaceStatistics_response.SerializeToString,
  }
  method_implementations = {
    ('telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', 'BrocadeTelemetryPhysicalInterfaceStatistics'): face_utilities.unary_stream_inline(servicer.BrocadeTelemetryPhysicalInterfaceStatistics),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_BrocadeTelemetryPhysicalInterfaceStatistics_service_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', 'BrocadeTelemetryPhysicalInterfaceStatistics'): BrocadeTelemetryPhysicalInterfaceStatistics_request.SerializeToString,
  }
  response_deserializers = {
    ('telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', 'BrocadeTelemetryPhysicalInterfaceStatistics'): BrocadeTelemetryPhysicalInterfaceStatistics_response.FromString,
  }
  cardinalities = {
    'BrocadeTelemetryPhysicalInterfaceStatistics': cardinality.Cardinality.UNARY_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'telemetry_intf_stats.BrocadeTelemetryPhysicalInterfaceStatistics_service', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
