from device import Comms
import socket

class UDPServer(Comms):
    """ UDPServer class inherits from Comms interface class """

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def open(self):
        self.sock.bind(("127.0.0.1", 12345))

    def close(self):
        self.sock.close()

    def write(self, data):
        self.sock.sendto(data, ("127.0.0.1", 12345))

    def read(self, num_bytes):
        self.sock.recvfrom(num_bytes)
        data,addr = self.sock.recvfrom(num_bytes)
        print(str(data))
        print(str(addr))

class UDPClient(Comms):
    """ UDPClient class inherits from Comms interface class """

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def open(self):
        super().open()

    def close(self):
        super().close()

    def write(self, data):
        self.sock.sendto(data, ("127.0.0.1", 12345))

    def read (self, num_bytes):
        self.sock.recvfrom(num_bytes)
        data,addr = self.sock.recvfrom(num_bytes)
        print(str(data))
        print(str(addr))


# For functional testing of the udp server and client refer to worked examples
if __name__ == '__main__':
    pass

