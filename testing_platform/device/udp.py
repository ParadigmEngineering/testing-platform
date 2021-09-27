from device import Comms
import socket

class UDPServer(Comms):
    """ UDPServer class inherits from Comms interface class """

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def open(self):
        self.sock.bind((self.address, self.port))

    def close(self):
        self.sock.close()

    def write(self, data):
        self.sock.sendto(data, (self.address, self.port))

    def read(self, num_bytes):
        data,addr = self.sock.recvfrom(num_bytes)
        return "Data: {dat}\nAddress: {address}".format(dat = data, address = addr)

class UDPClient(Comms):
    """ UDPClient class inherits from Comms interface class """

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def open(self):
        super().open()

    def close(self):
        super().close()

    def write(self, data):
        self.sock.sendto(data, (self.address, self.port))

    def read (self, num_bytes):
        data,addr = self.sock.recvfrom(num_bytes)
        return "Data: {dat}\n Address: {address}".format(dat = data, address = addr)


# For functional testing of the udp server and client refer to worked examples
if __name__ == '__main__':
    pass

