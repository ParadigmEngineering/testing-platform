import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = b"Hello UDP Server, this is UDP Client"
client_sock.sendto(msg, ("127.0.0.1", 12345))
data, addr = client_sock.recvfrom(4096)
print("Server Says")
print(str(data))
client_sock.close()
