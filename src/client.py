import grpc
import model3501_pb2
import model3501_pb2_grpc
import argparse

def list_devices(server_address):
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
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SetDeviceSpeed method
        response = stub.SetDeviceSpeed(model3501_pb2.SpeedRequest(speed_type=speed_type))
        print("Response from SetDeviceSpeed:", response.message)

def enumerate_charge(server_address, watts):
    with grpc.insecure_channel(server_address) as channel:
        stub = model3501_pb2_grpc.GreetingServiceStub(channel)

        # Call the SendData method
        response = stub.SendData(model3501_pb2.DataRequest(watts=watts))
        print("Response from EnumerateCharge:", response.message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC Client')
    parser.add_argument('server_ip', help='Server IP address')
    parser.add_argument('server_port', type=int, help='Server port number')
    parser.add_argument('action', choices=['list', 'set_speed', 'enumerateCharge'], help='Action to perform')
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
    else:
        print("Invalid action")
