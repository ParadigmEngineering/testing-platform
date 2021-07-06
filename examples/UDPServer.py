import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 12345))

while True:
    data, addr = sock.recvfrom(4096) #For sending data, use recv_from
    print(str(data))
    print(str(addr))
    msg = b"Hello, I am a UDP Server!"
    sock.sendto(msg, addr)
