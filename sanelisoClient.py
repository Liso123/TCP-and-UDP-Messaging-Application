from socket import *
from threading import *
from random import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.bind((serverName, randint(8000,9000)))

clientName = input("Enter your nickname: ")

def receive():
    while True:
        try:
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode())
        except:
            pass

t = Thread(target=receive)
t.start()

clientSocket.sendto(f"SIGNUP_TAG:{clientName}".encode(), (serverName, serverPort))

while True:
    message = input("Enter message: ")
    if message == "!q":
        exit()
    else:
        clientSocket.sendto(f"{clientName}: {message}".encode(), (serverName, serverPort))