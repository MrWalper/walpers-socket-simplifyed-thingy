import socket
import threading

class client():
    def __init__(self, username:str, host:str, port:int, logPacket:bool):
        self.username = username
        self.host = host
        self.port = port
        self.logPacket = logPacket

        self.clientSocket = socket.socket()
        self.latestPacket = ""

        try:
            self.clientSocket.connect((self.host,self.port))
            self.clientSocket.send(f"{self.username}:codename".encode())
        except ConnectionRefusedError:
            print("Couldn't connect to server.")
    
    def sendPacket(self, message:str):
        try:
            self.data = self.clientSocket.send(message.encode())
            if self.logPacket:
                print(self.data)
        except ConnectionResetError and ConnectionAbortedError:
            print("Conenction has been reseted! Attempting to re-connect")
            try:
                self.clientSocket.close()
                self.clientSocket = socket.socket()
                self.clientSocket.connect((self.host,self.port))
            except ConnectionRefusedError:
                print("Couldn't connect to server.")
    
    def listenToServer(self):
        while True:
            try:
                self.data = self.clientSocket.recv(self.port).decode()
                self.latestPacket = self.data
                if self.logPacket and len(self.data) >= 3:
                    print(self.data)
                    return("No data to print!")
            except ConnectionAbortedError and ConnectionResetError:
                print("Connection aborted!")
                quit()

if __name__ == "__main__":
    clientVar = client(username="Walper",host="localhost",port=5000,logPacket=True)
    listenThread = threading.Thread(target=clientVar.listenToServer)
    listenThread.start()

    while True:
        #listenThread.start()
        data = input("\n> ")
        clientVar.sendPacket(message=data)
    