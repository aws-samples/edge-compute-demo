# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/tap/v2alpha/tap.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.common.tap.v2alpha import common_pb2 as envoy_dot_config_dot_common_dot_tap_dot_v2alpha_dot_common__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.envoy/config/filter/http/tap/v2alpha/tap.proto\x12$envoy.config.filter.http.tap.v2alpha\x1a,envoy/config/common/tap/v2alpha/common.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"^\n\x03Tap\x12W\n\rcommon_config\x18\x01 \x01(\x0b\x32\x36.envoy.config.common.tap.v2alpha.CommonExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x42\xc1\x01\n2io.envoyproxy.envoy.config.filter.http.tap.v2alphaB\x08TapProtoP\x01ZKgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/tap/v2alpha\xf2\x98\xfe\x8f\x05&\x12$envoy.extensions.filters.http.tap.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.filter.http.tap.v2alpha.tap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n2io.envoyproxy.envoy.config.filter.http.tap.v2alphaB\010TapProtoP\001ZKgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/tap/v2alpha\362\230\376\217\005&\022$envoy.extensions.filters.http.tap.v3\272\200\310\321\006\002\020\001'
  _TAP.fields_by_name['common_config']._options = None
  _TAP.fields_by_name['common_config']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_TAP']._serialized_start=222
  _globals['_TAP']._serialized_end=316
# @@protoc_insertion_point(module_scope)
