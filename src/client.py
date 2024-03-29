
##############################################################################
# 
# Module: client.py
#
# Description:
# This script implements a gRPC client to interact with a Model 3501 SuperMUTT USB device.
# The client sends requests to the server and receives responses.
#
#     Released under the MCCI Corporation.
#
# Author:
#     Vinay N, MCCI Corporation
#
##############################################################################
import grpc
import model3501_pb2
import model3501_pb2_grpc
import argparse

def list_devices(server_address):
    """
    Method to list USB devices connected to the server.
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the FindUsbDevice method
        usb_response = stub.FindUsbDevice(model3501_pb2.FindUsbDeviceRequest(list_devices=True))
        
        for device in usb_response.devices:
            print("USB Device Info:")
            print("  Manufacturer:", device.manufacturer)
            print("  Product:", device.product)
            print("  Firmware Version:", device.firmware_version)

def set_speed(server_address, speed_type):
    """
    Method to set the speed of the USB device.
    speed type: speed type is super speed or high speed.
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SetDeviceSpeed method
        response = stub.SetDeviceSpeed(model3501_pb2.SpeedRequest(speed_type=speed_type))
        print("Response from SetDeviceSpeed:", response.message)

def enumerate_charge(server_address, watts):
    """
    Method to emulate charging on the USB device.
    watts: to set emulatecharge in watts.
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SendData method
        response = stub.SendData(model3501_pb2.DataRequest(watts=watts))
        print("Response from EnumerateCharge:", response.message)

def cd_stress_on(server_address):
    """
    Enable connect disconnect stress
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the CdStressOn method
        response = stub.CdStressOn(model3501_pb2.CdStressRequest())
        print("Response from CdStressOn:", response.message)

def cd_stress_off(server_address):
    """
    Disable connect disconnect stress
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the CdStressOff method
        response = stub.CdStressOff(model3501_pb2.CdStressOffRequest())
        print("Response from CdStressOff:", response.message)

def prswap(server_address):
    """
    Initiate power role swap
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SendPRswapCommand method
        response = stub.SendPRswapCommand(model3501_pb2.PRswapRequest())
        print("Response from PRswap command:", response.message)

def drswap(server_address):
    """
    Initiate data role swap
    """
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SendDRswapCommand method
        response = stub.SendDRswapCommand(model3501_pb2.DRswapRequest())
        print("Response from DRSWAP command:", response.message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC Client')
    parser.add_argument('server_ip', help='Server IP address')
    parser.add_argument('server_port', type=int, help='Server port number')
    parser.add_argument('action', choices=['list', 'set_speed', 'enumerateCharge', 'cd_stress_on','cd_stress_off', 'prswap', 'drswap'], help='Action to perform')
    parser.add_argument('value', nargs='?', help='Value for the action [s, h set the speed, W Emulate a PD charger with max W]')
    args = parser.parse_args()
    
    server_address = f"{args.server_ip}:{args.server_port}"
    
    if args.action == 'list':
        list_devices(server_address)
    elif args.action == 'set_speed':
        if args.value:
            set_speed(server_address, args.value)
        else:
            print("Speed type not provided. Please provide speed type (s for Super Speed, h for High Speed).")
    elif args.action == 'enumerateCharge':
        if args.value is not None:
            enumerate_charge(server_address, int(args.value))
        else:
            print("Watts not provided. Please provide watts.")
    elif args.action == 'cd_stress_on':
        cd_stress_on(server_address)
    
    elif args.action == 'cd_stress_off':
        cd_stress_off(server_address)

    elif args.action == 'prswap':
        prswap(server_address)
    elif args.action == 'drswap':
        drswap(server_address)
    else:
        print("Invalid action")
