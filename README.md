# Chat In Terminal 
Hello all. 😉 
Sockets and servers are vey important for connection and importantly chatting with others.😂😁
I have thought of making a python script which will amek connection and eventually allow us to chat.

(**DISCLAIMER** - This python script runs only on localhost. If you want to make a connection with other devices then you should check the code of the server.py file and use *network* library in the client.py file)🙃

# About 
So, the thing that is done with this script is that, it starts a server and with the help of threading maintains many clients.
It is like chatting in the terminal. You can join the chat by starting the *client.py* file.

![](https://github.com/Shreejan-35/Chat-App/blob/main/res/chat-img.jpg)

# Getting Started 😎😎
Working with it is very simple.
- There shouble be a host means the head of the chat
- The host should run the *server.py* file and note the password given by it.
- The host need to start another terminal and start *client.py* file and enter with name **host** 👩‍💻👩‍💻
- He/She needs to give the correct password as given by the server to start the chat. 🔐
- **Anyone cannot join the chat unless host has joined** 👥
- After host has joined, anyone can join now 👨‍👨‍👦‍👦👩‍👩‍👧‍👦
- Clients need to join with their nickname
- The message which will be send will be shown with their nickname in fron of the message

# Commands to execute and things need to be installed
**Python 3 need to be installed**
You do not need to install anything because all teh libraries used here are built-in.
- Sockets
- Threading
Commands - 
- 1. Run the server.py file
```
python3 server.py
```
- 2. Open another terminal and run the client.py and join as host and give the password
```
python client.py
```


(This is the video of the live example) - link to youtube - https://youtu.be/R8MLOCNbMu0
![](https://user-images.githubusercontent.com/93109967/153348980-3320af09-fb6d-4322-aa75-920daa84dd88.mp4)

## Contirbution
Feel free to contribute to this project

## License
GNU Public License
