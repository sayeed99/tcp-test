import socket

TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = f"Hello from client {socket.gethostname()}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())

try:
    while True:
        data = s.recv(BUFFER_SIZE)
        print(f"Boradcast Data : {data.decode()}")
        x = input("Enter message : ")
        s.send(x.encode())
except KeyboardInterrupt:
    s.close()
    print("\nClient closed.")
