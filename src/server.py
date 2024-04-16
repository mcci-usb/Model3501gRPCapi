##############################################################################
# 
# Module: server.py
#
# Description:
#     This script implements a gRPC server providing services to interact with a 
#     Model 3501 SuperMUTT USB device.
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
    def SayHi(self, request, context):
        # return model3501_pb2.HiResponse(message=f"Hi, {request.name}!")
        pass

    def SayHello(self, request, context):
        # return model3501_pb2.HelloResponse(message=f"Hello, {request.name}!")
        pass

    def FindUsbDevice(self, request, context):
        """
        Method to find USB devices connected to the system.
        List Type-C MUTTs by index.
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
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # request parameter holds the request message sent by the client.
        speed_type = request.speed_type
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            # Context information about the RPC, including 
            # handling deadlines and cancellations.
            return model3501_pb2.SpeedResponse(message="Device not found")

        #This method sets the active configuration for the USB device
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
        Set to speed 'S'. Options are Full, High, or Super. Or read back
        current speed if no option passed in.
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
        Emulate a PD charger with max watts 'W'
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
        device: device as the USB device object
        watts:watts as the data to be sent to the USB device.
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
    
    def CdStressOn(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # To update the status for cmd sent success or failed.
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.CdStressResponse(message="Device not found")

        # Call the function to send the control transfer
        success = self.cd_stress_on(device)

        if success:
            print("CD Stress On command sent successfully")
            return model3501_pb2.CdStressResponse(message="CD Stress On command sent successfully")
        else:
            print("Failed to send CD Stress On command")
            return model3501_pb2.CdStressResponse(message="Failed to send CD Stress On command")

    def cd_stress_on(self, device):
        """
        Enable connect disconnect stress.
    
        """
        # Enable connect disconnect stress
        bmRequestType = 0x40
        bRequest = 0xE8
        wValue = 0x00
        wIndex = 0x1
        wLength = 0x00

        # Send control transfer
        result = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        return result == 0
    
    def CdStressOff(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # To update the status for cmd sent success or failed.
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.CdStressResponse(message="Device not found")

        # Call the function to send the control transfer
        success = self.cd_stress_off(device)

        if success:
            print("CD Stress Off command sent successfully")
            return model3501_pb2.CdStressResponse(message="CD Stress Off command sent successfully")
        else:
            print("Failed to send CD Stress Off command")
            return model3501_pb2.CdStressResponse(message="Failed to send CD Stress Off command")

    def cd_stress_off(self, device):
        """
        Disable connect disconnect stress
        """
        # Disable connect disconnect stress
        bmRequestType = 0x40  # Request type: Vendor, Host-to-device, Device-to-interface
        bRequest = 0xE8      # Request code for CD Stress Off command
        wValue = 0x0000       # Value
        wIndex = 0x0000       # Index
        wLength = 0x0000      # Length

        # Send control transfer
        result = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        return result == 0
    #----------------------------------------------------------------
    def PdCaptiveCable(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # Find the USB device
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.PdCaptiveCableResponse(message="Device not found")

        # Perform PdCaptiveCable operation
        success = self.pd_captive_cable(device)

        if success:
            print("PdCaptiveCable command sent successfully")
            return model3501_pb2.PdCaptiveCableResponse(message="PdCaptiveCable command sent successfully")
        else:
            print("Failed to send PdCaptiveCable command")
            return model3501_pb2.PdCaptiveCableResponse(message="Failed to send PdCaptiveCable command")

    def pd_captive_cable(self, device):
        """
        Switch PD to captive cable
        """
        # Control transfer parameters for PdCaptiveCable
        bmRequestType = 0x40  # Request type: Vendor, Host-to-device, Device-to-interface
        bRequest = 0xE9       # Request code for PdCaptiveCable command
        wValue = 0x0000       # Value
        wIndex = 0x0000       # Index
        wLength = 0x0000      # Length

        # Send control transfer for PdCaptiveCable command
        result = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        return result == 0

    #-----------------------------PD-CAPTIVE-CABLE-END--------------------------------
    
    #----------------------------------------------------------------
    def PdChargerPort(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # Find the USB device
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.PdChargerPortResponse(message="Device not found")

        # Perform PdCaptiveCable operation
        success = self.pd_charger_port(device)

        if success:
            print("PdChargerPort command sent successfully")
            return model3501_pb2.PdChargerPortResponse(message="PdCaptiveCable command sent successfully")
        else:
            print("Failed to send PdChargerPort command")
            return model3501_pb2.PdChargerPortResponse(message="Failed to send PdCaptiveCable command")

    def pd_charger_port(self, device):
        """
        Switch PD to charger receptacle
        """
        # Control transfer parameters for PdCaptiveCable
        bmRequestType = 0x40  # Request type: Vendor, Host-to-device, Device-to-interface
        bRequest = 0xE9       # Request code for PdCaptiveCable command
        wValue = 0x0000       # Value
        wIndex = 0x0001       # Index
        wLength = 0x0000      # Length

        # Send control transfer for PdCaptiveCable command
        result = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        return result == 0

    #----------------------------------------------------------------
   
    def SendPRswapCommand(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # Initiate power role swap
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.PRswapResponse(message="Device not found")

        # Data for PRswap command
        data_prswap = [0x00, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

        # Send control transfer for PRswap command
        result_prswap = device.ctrl_transfer(0x40, 0xE4, 0x0000, 0x0000, data_prswap)

        return model3501_pb2.PRswapResponse(message="Control transfer result for PRswap command:\n{}".format(result_prswap))

    def SendDRswapCommand(self, request, context):
        """
        self: This is reference to the instance of the class.
        request:This parameter holds the request message sent by the client.
        context:Provides contextual information about the RPC, 
        including handling deadlines and cancellations.
        """
        # Initiate data role swap
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            print("Device not found")
            return model3501_pb2.DRswapResponse(message="Device not found")

        # Data for DRSWAP command
        data_drswap = [0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

        # Send control transfer for DRSWAP command
        result_drswap = device.ctrl_transfer(0x40, 0xE4, 0x0000, 0x0000, data_drswap)

        return model3501_pb2.DRswapResponse(message="Control transfer result for DRSWAP command:\n{}".format(result_drswap))

    def GetPowerRole(self, request, context):
        """
        Read the current power role
        """
        # Find the USB device
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            return model3501_pb2.GetPowerRoleResponse(power_role=model3501_pb2.INVALID)

        # Set configuration
        device.set_configuration()

        # First control transfer (HOST to DEVICE)
        bmRequestType = 0x40  # Request type: Vendor, Host-to-device, Device-to-interface
        bRequest = 0xE4        # Request code
        wValue = 0x0000        # Value
        wIndex = 0x0000        # Index
        wLength = 0x0010       # Length

        data1 = [0x00, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

        result1 = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data1)

        if result1 != 16:
            return model3501_pb2.GetPowerRoleResponse(power_role=model3501_pb2.INVALID)

        # Second control transfer (HOST to DEVICE)
        bmRequestType = 0xC0  # Request type: Vendor, Device-to-host, Device-to-interface
        bRequest = 0xE4        # Request code
        wValue = 0x0000        # Value
        wIndex = 0x0000        # Index
        wLength = 0x0010       # Length

        result2 = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)

        hex_strings = ['0x{:02X}'.format(byte) for byte in result2]
        formatted_hex_string = ' '.join(hex_strings)
        
        sink_data = "0x00 0x28 0x02 0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"
        source_data = "0x00 0x28 0x02 0x02 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00"

        if formatted_hex_string == sink_data:
            return model3501_pb2.GetPowerRoleResponse(power_role=model3501_pb2.SINK)
        elif formatted_hex_string == source_data:
            return model3501_pb2.GetPowerRoleResponse(power_role=model3501_pb2.SOURCE)
        else:
            return model3501_pb2.GetPowerRoleResponse(power_role=model3501_pb2.INVALID)
    
    def GetRdo(self, request, context):
        """
        Read the RDO for the current power contract
        """
        device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if device is None:
            return model3501_pb2.GetRdoResponse(rdo_data="Device not found")
        
        device.set_configuration()
        
        bmRequestType = 0x40  # Request type: Vendor, Host-to-device, Device-to-interface
        bRequest = 0xE4        # Request code
        wValue = 0x0000        # Value
        wIndex = 0x0000        # Index
        wLength = 0x0010       # Length
        
        data1 = [0x00, 0x2A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        
        result1 = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data1)
        
        if result1 == 16:
            bmRequestType = 0xC0  # Request type: Vendor, Device-to-host, Device-to-interface
            bRequest = 0xE4        # Request code
            wValue = 0x0000        # Value
            wIndex = 0x0000        # Index
            wLength = 0x0010       # Length
        
            result2 = device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, wLength)
        
            hex_strings = ['0x{:02X}'.format(byte) for byte in result2]
            formatted_hex_string = ' '.join(hex_strings)
            
            return model3501_pb2.GetRdoResponse(rdo_data=formatted_hex_string)
        
        else:
            return model3501_pb2.GetRdoResponse(rdo_data="Invalid command")
        
def serve(port):
    """
    Method to start the gRPC server with port.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model3501_pb2_grpc.add_GreetingServiceServicer_to_server(GreetingService(), server)
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    print("Model3501grpcapi-V1.3.0")
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
