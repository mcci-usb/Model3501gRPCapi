# Model3501Grpcapi

This repository serves as a comprehensive source code for Model3501Grpcapi, which facilitates communication between client and server models using gRPC (Google Remote Procedure Call)

## gRPC – An RPC library and framework

gRPC is a modern, open source, high-performance remote procedure call (RPC) framework that can run anywhere. gRPC enables client and server applications to communicate transparently, and simplifies the building of connected systems.

## Prerequisites for running or building

### Install Python (if not already installed)

Install python package from [python.org](https://www.python.org/ftp/python/3.7.8/python-3.7.8.exe)

### Install/upgrade pip

```shell
pip --version
python -m pip install --upgrade pip
```

### Install python packages

Use the following steps to install the required libraries:

1. Open a command prompt or terminal.
2. Run the following commands to install the python dependency libraries:

* pyusb  - 1.2.1
* grpcio - 1.60.1
* protobuf - 4.25.3
* grpcio-tools - 1.60.1

```shell
pip install pyusb
pip install grpcio
pip install protobuf
```

## Installing Import Libraries

1. Clone the repository from [Github](https://github.com/mcci-usb/Model3501gRPCapi)

2. Open a `cmd prompt` and change directory to  `{path_to_repository}/Model3501gRPCapi`. using `cd` into the root directory where setup.py is located

## Run Server

To run the server script, execute the following command in your terminal:

```shell
python server.py <port_number>
```

Replace <port_number> with the desired port number where the server should listen for incoming connections.

## Run Client

To run the client script, execute the following command in your terminal:

```shell
python client.py <server_ip> <port_number> <cmd> <value>
```

```shell
Note: Here both server.py and client.py run into difftrent machines.

```

Replace `server_ip` with the IP address of the server, `port_number` with the port number where the server is listening for incoming connections, `cmd` with the desired command, and `value` with the corresponding value for the command.

```shell
Note: The server and client run on different machines.
```

## cmd line arguments to Server

* argument 1: `server.py`
* argument 2: `port_number`

**NOTE:**

* example of port_number

```shell
python server.py 2023
```

## cmd line arguments to Client

* argument 1: `client.py`
* argument 2: `server_ip_address`
* argument 3: `server_port_number`
* argument 4: `action`
* argument 5: `value`

**NOTE:**

```shell
python client.py 192.168.x.xx 2023 -h

python client.py 192.168.x.xx 2023 list

python client.py 192.168.x.xx 2023 set_speed s #(set super speed)

python client.py 192.168.x.xx 2023 set_speed h #(set high speed)

python client.py 192.168.x.xx 2023 enumerateCharge 40

```

## Demo Video (Server)

![Demo Video](assets/Model3501-gRpc-server.gif)

## Demo Video (Client)

![Demo Video](assets/Model3501-gRpc-client.gif)
