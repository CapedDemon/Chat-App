import socket
import threading
import random
import time

IP = ""
server_IP = socket.gethostbyname(IP)

mainServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainServer.bind((IP, 1241))
mainServer.listen()

password = random.randint(1, 1000)
password = password/2

print("Server is listening...")
print(f"Join as a host with another client open and give this as your password - {password}")

clientNames = []
banned = []
sockets_clients = []

def broadcast(message):
    for clients in sockets_clients:
        clients.send(bytes(message, "utf-8"))
    
def messaging(client):
    while True:
        try:
            msg = client.recv(1024)
            msg = msg.decode("utf-8")
            broadcast(msg)
        except:
            
            clientIndex = sockets_clients.index(client)
            sockets_clients.pop(clientIndex)
            socketLeave = clientNames[clientIndex]
            leavemessage = f"{socketLeave} has left the meeting"
            broadcast(leavemessage)
            clientNames.pop(clientIndex)
            break
        

def receive():
    while True:
        clientsocket, address = mainServer.accept()
        nickname = clientsocket.recv(1024)
        nickname = nickname.decode("utf-8")

        if "host" in clientNames:
            sockets_clients.append(clientsocket)

            
            clientNames.append(nickname)

            print(f"Connected with {clientsocket}.\n")

            msg = f"{nickname} joined!"
            broadcast(msg)

            thread = threading.Thread(target=messaging, args=(clientsocket, ))
            thread.start()
        
        elif nickname == "host":
            clientsocket.send(bytes("Enter the password: ", "utf-8"))
            passwordCheck = clientsocket.recv(1024)
            passwordCheck = passwordCheck.decode("utf-8")
            usrpass = str(password)
            print(passwordCheck)
            if passwordCheck == usrpass:
                sockets_clients.append(clientsocket)
                clientNames.append("host")
                print("Connect with host")
                msg = f"Host Joined!"
                broadcast(msg)
                thread = threading.Thread(target=messaging, args=(clientsocket, ))
                thread.start()
            else:
                clientsocket.close()
                continue
        
        elif nickname in clientNames:
            
            clientsocket.send(bytes("Name already exist!!", "utf-8"))
            clientsocket.close()

        elif nickname in banned:
            clientsocket.close()

        else:
            
            clientsocket.send(bytes("Host not joined yet!!", "utf-8"))
            clientsocket.close()

receive()