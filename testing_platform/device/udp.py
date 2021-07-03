import comms
import socket

class UDPServer(Comms):
    """ UDPServer class inherits from Comms interface class """

    def __init__(self, sock):
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

    def __init__(self, sock):
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


# Maybe use this for functional testing of the classes in this file,
# not sure if this is good practice though
if __name__ == '__main__':
    server_sock, client_sock = socket

    server = UDPServer(server_sock)
    server.open()
    server.write(b"Hello, I am a UDP Server!")

    client = UDPClient(client_sock)
    client.open()
    client.write(b"Hello UDP Server, this is UDP Client")

    server.read(4096)
    client.read(4096)

    server.close()
    client.close()
    
    pass

