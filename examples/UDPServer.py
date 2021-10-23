import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 12345))

    try:
        print("Press Ctrl+C to terminate the loop checking for data from UDPClient.")
        while True:
            data, addr = sock.recvfrom(4096) #For sending data, use recv_from
            print(str(data))
            print(str(addr))
            msg = b"Hello, I am a UDP Server!"
            sock.sendto(msg, addr)
    except KeyboardInterrupt:
        print("\nCtrl+C terminated the loop.")
        pass

if __name__ == '__main__':
    main()
