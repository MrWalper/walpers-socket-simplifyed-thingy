import socket

class client():
    def __init__(self, username:str, host:str, port:int, logPacket:bool):
        self.username = username
        self.host = host
        self.port = port
        self.logPacket = logPacket

        self.testMessage = "Walper"
        self.clientSocket = socket.socket()
        try:
            self.clientSocket.connect((self.host,self.port))
        except ConnectionRefusedError:
            print("Couldn't connect to server.")
    
    def sendPacket(self, message:str):
        self.data = self.clientSocket.send(message.encode())
        if self.logPacket:
            print(self.data)
        return self.data
    
    def listenToServer(self):
        self.data = self.clientSocket.recv(self.port).decode()
        if self.logPacket:
            print(self.data)

clientVar = client(username="Walper",host="localhost",port=5000,logPacket=True)
while True:
    data = input("> ")
    clientVar.sendPacket(data)
    data = clientVar.listenToServer()
    if data:
        print(data)