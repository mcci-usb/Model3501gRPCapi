##############################################################################
# 
# Module: server.py
#
# Description:
#     This script implements a gRPC server providing services to interact with a 
#     Model 3501 SuperMUTT USB device.
#
# Copyright notice:
#     This file copyright (c) 2024 by
#
#         MCCI Corporation
#         3520 Krums Corners Road
#         Ithaca, NY  14850
#
#     Released under the MCCI Corporation.
#
# Author:
#     Vinay N, MCCI Corporation
#
##############################################################################

import sys
import grpc
from concurrent import futures
import model3501_pb2
import model3501_pb2_grpc
import usb.core
import usb.util


# Constants defining USB device vendor and product IDs
VENDOR_ID = 0x045E  # Example VID (Microsoft)
PRODUCT_ID = 0x078F  # Example PID

class GreetingService(model3501_pb2_grpc.GreetingServiceServicer):
    """
    Implementation of the gRPC service methods.
    """
    def SayHi(self, request, context):
        # return model3501_pb2.HiResponse(message=f"Hi, {request.name}!")
        pass

    def SayHello(self, request, context):
        # return model3501_pb2.HelloResponse(message=f"Hello, {request.name}!")
        pass

    def FindUsbDevice(self, request, context):
        """
        Method to find USB devices connected to the system.
        self: This is a reference to the instance of the class GreetingService. 
        request: This parameter represents the request object sent by the client.
        context: This parameter provides contextual information about the RPC call
        """
        if request.list_devices:
            devices_info = []

            # Find all USB devices connected to the system
            devices = usb.core.find(find_all=True)

            # Iterate through each device and check if it matches the target VID and PID
            for device in devices:
                # Check if the device has both VID and PID attributes
                if device.idVendor is not None and device.idProduct is not None:
                    # Check if the device matches the target VID and PID
                    if device.idVendor == VENDOR_ID and device.idProduct == PRODUCT_ID:
                        # Retrieve device information
                        manufacturer = usb.util.get_string(device, device.iManufacturer)
                        product = usb.util.get_string(device, device.iProduct)
                        firmware_version = device.bcdDevice

                        # Create a UsbDevice object and append it to the list of devices
                        device_info = model3501_pb2.UsbDevice(
                            manufacturer=manufacturer,
                            product=product,
                            firmware_version=firmware_version
                        )
                        devices_info.append(device_info)

            # Create the response with the list of devices
            response = model3501_pb2.FindUsbDeviceResponse(devices=devices_info)
            return response

        else:
            # Handle other cases if needed
            pass
    
    def SetDeviceSpeed(self, request, context):
        """
        Method to set the speed of the USB device.
        self: This is a reference to the instance of the class GreetingService. 
        request: This parameter represents the request object sent by the client.
        context: This parameter provides contextual information about the RPC call
        """
        speed_type = request.speed_type
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.SpeedResponse(message="Device not found")

        device.set_configuration()

        if speed_type == 's':
            success = self.set_device_speed(device, 's')
            speed = "Super Speed"
        elif speed_type == 'h':
            success = self.set_device_speed(device, 'h')
            speed = "High Speed"
        else:
            print("Invalid speed type")
            return model3501_pb2.SpeedResponse(message="Invalid speed type")

        if success:
            print(f"{speed} set successfully")
            return model3501_pb2.SpeedResponse(message=f"{speed} set successfully")
        else:
            print("Failed to set speed")
            return model3501_pb2.SpeedResponse(message="Failed to set speed")
    
    def set_device_speed(self, device, speed_type):
        """
        Method to set the speed of the USB device.
        self: This is a reference to the instance of the class GreetingService. 
        request: This parameter represents the request object sent by the client. I
        context: This parameter provides contextual information about the RPC call
        """
        bmRequestType = 0x40
        if speed_type == 's':
            bRequest = 0x15  # Super Speed request
        elif speed_type == 'h':
            bRequest = 0x14  # High Speed request
        else:
            return False

        wValue = 0x0000
        wIndex = 0x0000
        wLength = 0x0000

        result = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        return result == 0
     
    def SendData(self, request, context):
        """
        Method to send data to the USB device.
        self: This is a reference to the instance of the class GreetingService. 
        request: This parameter represents the request object sent by the client. I
        context: This parameter provides contextual information about the RPC call
        """
        watts = request.watts
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.DataResponse(message="Device not found")

        # Send data with the specified watts
        success = self.send_data(device, watts)

        if success:
            print(f"Data sent successfully with {watts} watts")
            return model3501_pb2.DataResponse(message=f"Data sent successfully with {watts} watts")
        else:
            print("Failed to send data")
            return model3501_pb2.DataResponse(message="Failed to send data")

    def send_data(self, device, watts):
        """
        Method to send watts data to the USB device.
        self: This is a reference to the instance of the class GreetingService. 
        request: This parameter represents the request object sent by the client. I
        context: This parameter provides contextual information about the RPC call
        """
        bmRequestType_ctrl = 0x40
        bRequest_ctrl = 0xED
        wValue_ctrl = 0x0000
        wIndex_ctrl = 0x0000
        wLength_ctrl = 0x0004

        bmRequestType_setup = 0x40
        bRequest_setup = 0xEE
        
        if watts <= 15:
            data_to_send_setup = [0x01, 0x01, 0xC8, 0x90, 0x01, 0x04]
            wValue_setup = 0x0000
        elif watts <= 27:
            data_to_send_setup = [0x01, 0x02, 0x2C, 0x91, 0x01, 0x04]
            wValue_setup = 0x0001
        elif watts <= 45:
            data_to_send_setup = [0x01, 0x03, 0x2C, 0x91, 0x01, 0x04, 0x2C]
            wValue_setup = 0x0002
        else:
            return False  # Invalid wattage

        # Send setup control transfer
        result_setup = device.ctrl_transfer(bmRequestType_setup, bRequest_setup, wValue_setup, wIndex_ctrl, data_to_send_setup)
        print("Setup control transfer result:", result_setup)

        # Send control transfer with payload
        result_ctrl = device.ctrl_transfer(bmRequestType_ctrl, bRequest_ctrl, wValue_ctrl, wIndex_ctrl)
        # print("Control transfer result:", result_ctrl)

        return True

def serve(port):
    """
    Method to start the gRPC server.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model3501_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    print("Model3501grpcapi-V1.0.0")
    print("Server started. Listening on port", port, "...")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Stopping the server...")
        server.stop(0)

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    serve(port)
