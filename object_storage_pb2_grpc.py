# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import object_storage_pb2 as object__storage__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in object_storage_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ObjectStorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.stream_unary(
                '/objectStorage.ObjectStorage/Upload',
                request_serializer=object__storage__pb2.File.SerializeToString,
                response_deserializer=object__storage__pb2.UploadResponse.FromString,
                _registered_method=True)
        self.Get = channel.unary_stream(
                '/objectStorage.ObjectStorage/Get',
                request_serializer=object__storage__pb2.GetRequest.SerializeToString,
                response_deserializer=object__storage__pb2.File.FromString,
                _registered_method=True)


class ObjectStorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.stream_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=object__storage__pb2.File.FromString,
                    response_serializer=object__storage__pb2.UploadResponse.SerializeToString,
            ),
            'Get': grpc.unary_stream_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=object__storage__pb2.GetRequest.FromString,
                    response_serializer=object__storage__pb2.File.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'objectStorage.ObjectStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('objectStorage.ObjectStorage', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ObjectStorage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/objectStorage.ObjectStorage/Upload',
            object__storage__pb2.File.SerializeToString,
            object__storage__pb2.UploadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/objectStorage.ObjectStorage/Get',
            object__storage__pb2.GetRequest.SerializeToString,
            object__storage__pb2.File.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
