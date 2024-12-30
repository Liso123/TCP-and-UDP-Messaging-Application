from socket import *
from queue import *
from threading import *

messages = Queue()
clients = []
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 12000

serverSocket.bind(("localhost", serverPort))

def receive():
    while True:
        try:
            message, clientAddress = serverSocket.recvfrom(2048) #What is 2048?
            messages.put((message, clientAddress))
        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            message, clientAddress = messages.get()
            print(message.decode())
            if clientAddress not in clients:
                clients.append(clientAddress)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG:"):
                        clientName = message.decode()[messages.decode().index(":")+1:]
                        serverSocket.sendto(f"{clientName} joined!".encode(), client)
                    else:
                        serverSocket.sendto(message, client)
                except:
                    clients.remove(client)

t1 = Thread(target=receive)
t2 = Thread(target=broadcast)

t1.start()
t2.start()
