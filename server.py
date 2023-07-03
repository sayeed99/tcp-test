import socket
import threading

TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024
WELCOME_MSG = "Welcome to the server"
clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

def handle_client(c, addr):
    c.send(WELCOME_MSG.encode())
    while True:
        data = c.recv(BUFFER_SIZE)
        if not data:
            break
        broadcast(data, addr)
    c.close()
    del clients[addr]

def broadcast(data, from_addr):
    print("Connected to : ", from_addr, "Data : ", data)
    for addr in clients:
        if addr != from_addr:
            try:
                clients[addr].send(data)
            except:
                pass

while True:
    conn, addr = s.accept()
    clients[addr] = conn
    threading.Thread(target=handle_client, args=(conn, addr)).start()
