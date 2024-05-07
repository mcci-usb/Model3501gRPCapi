# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import model3501_pb2 as model3501__pb2


class GreetingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHi = channel.unary_unary(
                '/hi_hello.GreetingService/SayHi',
                request_serializer=model3501__pb2.HiRequest.SerializeToString,
                response_deserializer=model3501__pb2.HiResponse.FromString,
                )
        self.SayHello = channel.unary_unary(
                '/hi_hello.GreetingService/SayHello',
                request_serializer=model3501__pb2.HelloRequest.SerializeToString,
                response_deserializer=model3501__pb2.HelloResponse.FromString,
                )
        self.FindUsbDevice = channel.unary_unary(
                '/hi_hello.GreetingService/FindUsbDevice',
                request_serializer=model3501__pb2.FindUsbDeviceRequest.SerializeToString,
                response_deserializer=model3501__pb2.FindUsbDeviceResponse.FromString,
                )
        self.SetDeviceSpeed = channel.unary_unary(
                '/hi_hello.GreetingService/SetDeviceSpeed',
                request_serializer=model3501__pb2.SpeedRequest.SerializeToString,
                response_deserializer=model3501__pb2.SpeedResponse.FromString,
                )
        self.SendData = channel.unary_unary(
                '/hi_hello.GreetingService/SendData',
                request_serializer=model3501__pb2.DataRequest.SerializeToString,
                response_deserializer=model3501__pb2.DataResponse.FromString,
                )
        self.CdStressOn = channel.unary_unary(
                '/hi_hello.GreetingService/CdStressOn',
                request_serializer=model3501__pb2.CdStressRequest.SerializeToString,
                response_deserializer=model3501__pb2.CdStressResponse.FromString,
                )
        self.CdStressOff = channel.unary_unary(
                '/hi_hello.GreetingService/CdStressOff',
                request_serializer=model3501__pb2.CdStressOffRequest.SerializeToString,
                response_deserializer=model3501__pb2.CdStressOffResponse.FromString,
                )
        self.SendPRswapCommand = channel.unary_unary(
                '/hi_hello.GreetingService/SendPRswapCommand',
                request_serializer=model3501__pb2.PRswapRequest.SerializeToString,
                response_deserializer=model3501__pb2.PRswapResponse.FromString,
                )
        self.SendDRswapCommand = channel.unary_unary(
                '/hi_hello.GreetingService/SendDRswapCommand',
                request_serializer=model3501__pb2.DRswapRequest.SerializeToString,
                response_deserializer=model3501__pb2.DRswapResponse.FromString,
                )
        self.PdCaptiveCable = channel.unary_unary(
                '/hi_hello.GreetingService/PdCaptiveCable',
                request_serializer=model3501__pb2.PdCaptiveCableRequest.SerializeToString,
                response_deserializer=model3501__pb2.PdCaptiveCableResponse.FromString,
                )
        self.PdChargerPort = channel.unary_unary(
                '/hi_hello.GreetingService/PdChargerPort',
                request_serializer=model3501__pb2.PdChargerPortRequest.SerializeToString,
                response_deserializer=model3501__pb2.PdChargerPortResponse.FromString,
                )
        self.GetPowerRole = channel.unary_unary(
                '/hi_hello.GreetingService/GetPowerRole',
                request_serializer=model3501__pb2.GetPowerRoleRequest.SerializeToString,
                response_deserializer=model3501__pb2.GetPowerRoleResponse.FromString,
                )
        self.GetRdo = channel.unary_unary(
                '/hi_hello.GreetingService/GetRdo',
                request_serializer=model3501__pb2.GetRdoRequest.SerializeToString,
                response_deserializer=model3501__pb2.GetRdoResponse.FromString,
                )
        self.ReconnectDevice = channel.unary_unary(
                '/hi_hello.GreetingService/ReconnectDevice',
                request_serializer=model3501__pb2.ReconnectRequest.SerializeToString,
                response_deserializer=model3501__pb2.ReconnectResponse.FromString,
                )


class GreetingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindUsbDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDeviceSpeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CdStressOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CdStressOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPRswapCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendDRswapCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PdCaptiveCable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PdChargerPort(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPowerRole(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRdo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReconnectDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHi': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHi,
                    request_deserializer=model3501__pb2.HiRequest.FromString,
                    response_serializer=model3501__pb2.HiResponse.SerializeToString,
            ),
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=model3501__pb2.HelloRequest.FromString,
                    response_serializer=model3501__pb2.HelloResponse.SerializeToString,
            ),
            'FindUsbDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.FindUsbDevice,
                    request_deserializer=model3501__pb2.FindUsbDeviceRequest.FromString,
                    response_serializer=model3501__pb2.FindUsbDeviceResponse.SerializeToString,
            ),
            'SetDeviceSpeed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDeviceSpeed,
                    request_deserializer=model3501__pb2.SpeedRequest.FromString,
                    response_serializer=model3501__pb2.SpeedResponse.SerializeToString,
            ),
            'SendData': grpc.unary_unary_rpc_method_handler(
                    servicer.SendData,
                    request_deserializer=model3501__pb2.DataRequest.FromString,
                    response_serializer=model3501__pb2.DataResponse.SerializeToString,
            ),
            'CdStressOn': grpc.unary_unary_rpc_method_handler(
                    servicer.CdStressOn,
                    request_deserializer=model3501__pb2.CdStressRequest.FromString,
                    response_serializer=model3501__pb2.CdStressResponse.SerializeToString,
            ),
            'CdStressOff': grpc.unary_unary_rpc_method_handler(
                    servicer.CdStressOff,
                    request_deserializer=model3501__pb2.CdStressOffRequest.FromString,
                    response_serializer=model3501__pb2.CdStressOffResponse.SerializeToString,
            ),
            'SendPRswapCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPRswapCommand,
                    request_deserializer=model3501__pb2.PRswapRequest.FromString,
                    response_serializer=model3501__pb2.PRswapResponse.SerializeToString,
            ),
            'SendDRswapCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendDRswapCommand,
                    request_deserializer=model3501__pb2.DRswapRequest.FromString,
                    response_serializer=model3501__pb2.DRswapResponse.SerializeToString,
            ),
            'PdCaptiveCable': grpc.unary_unary_rpc_method_handler(
                    servicer.PdCaptiveCable,
                    request_deserializer=model3501__pb2.PdCaptiveCableRequest.FromString,
                    response_serializer=model3501__pb2.PdCaptiveCableResponse.SerializeToString,
            ),
            'PdChargerPort': grpc.unary_unary_rpc_method_handler(
                    servicer.PdChargerPort,
                    request_deserializer=model3501__pb2.PdChargerPortRequest.FromString,
                    response_serializer=model3501__pb2.PdChargerPortResponse.SerializeToString,
            ),
            'GetPowerRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPowerRole,
                    request_deserializer=model3501__pb2.GetPowerRoleRequest.FromString,
                    response_serializer=model3501__pb2.GetPowerRoleResponse.SerializeToString,
            ),
            'GetRdo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRdo,
                    request_deserializer=model3501__pb2.GetRdoRequest.FromString,
                    response_serializer=model3501__pb2.GetRdoResponse.SerializeToString,
            ),
            'ReconnectDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ReconnectDevice,
                    request_deserializer=model3501__pb2.ReconnectRequest.FromString,
                    response_serializer=model3501__pb2.ReconnectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hi_hello.GreetingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SayHi',
            model3501__pb2.HiRequest.SerializeToString,
            model3501__pb2.HiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SayHello',
            model3501__pb2.HelloRequest.SerializeToString,
            model3501__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindUsbDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/FindUsbDevice',
            model3501__pb2.FindUsbDeviceRequest.SerializeToString,
            model3501__pb2.FindUsbDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetDeviceSpeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SetDeviceSpeed',
            model3501__pb2.SpeedRequest.SerializeToString,
            model3501__pb2.SpeedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SendData',
            model3501__pb2.DataRequest.SerializeToString,
            model3501__pb2.DataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CdStressOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/CdStressOn',
            model3501__pb2.CdStressRequest.SerializeToString,
            model3501__pb2.CdStressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CdStressOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/CdStressOff',
            model3501__pb2.CdStressOffRequest.SerializeToString,
            model3501__pb2.CdStressOffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPRswapCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SendPRswapCommand',
            model3501__pb2.PRswapRequest.SerializeToString,
            model3501__pb2.PRswapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendDRswapCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/SendDRswapCommand',
            model3501__pb2.DRswapRequest.SerializeToString,
            model3501__pb2.DRswapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PdCaptiveCable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/PdCaptiveCable',
            model3501__pb2.PdCaptiveCableRequest.SerializeToString,
            model3501__pb2.PdCaptiveCableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PdChargerPort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/PdChargerPort',
            model3501__pb2.PdChargerPortRequest.SerializeToString,
            model3501__pb2.PdChargerPortResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPowerRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/GetPowerRole',
            model3501__pb2.GetPowerRoleRequest.SerializeToString,
            model3501__pb2.GetPowerRoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRdo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/GetRdo',
            model3501__pb2.GetRdoRequest.SerializeToString,
            model3501__pb2.GetRdoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReconnectDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hi_hello.GreetingService/ReconnectDevice',
            model3501__pb2.ReconnectRequest.SerializeToString,
            model3501__pb2.ReconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
