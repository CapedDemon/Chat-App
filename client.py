import socket
from subprocess import STARTF_USESHOWWINDOW
import threading
import tkinter

nickname = input("Put your nickname: ")

class Client:
    invalid = False
    def __init__(self, host, port):
        self.clientServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientServer.connect((host, port))

        self.clientServer.send(bytes(nickname, "utf-8"))

        rThread = threading.Thread(target=self.receive)
        wThread = threading.Thread(target=self.write)

        rThread.start()
        wThread.start()

    def receive(self):
        while True:
            try:
                msg = self.clientServer.recv(2048)
                msg = msg.decode("utf-8")
                if msg == "Host not joined yet!!" or msg == "Name already exist!!":
                    self.invalid = True
                    break
                if msg == "Enter the password: ":
                    passwordCheck = input("Enter the password: ")
                    self.clientServer.send(bytes(passwordCheck, "utf-8"))
                else:
                    print(msg)
            except:
                break

    def write(self):
        while True and self.invalid == False:
            usermsg = input()
            usermsg = f"{nickname}: " + usermsg
            self.clientServer.send(bytes(usermsg, "utf-8"))

newClient = Client("127.0.0.1", 1241)