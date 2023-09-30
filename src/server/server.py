import socket
import threading
import json

def getJson(path:str):
    with open(path,"r") as file:
        data = json.load(file)
        return data
    
def listenToClients(addr:str,logPackets:bool):
    connectionDic[addr][0].send(b"Your listening thread made successfully")
    while True:
        global latestPacket
        latestPacket = connectionDic[addr][0].recv(5000)
        if logPackets:
                print(f"{addr}:{latestPacket.decode()}")

class server():
    def __init__(self):
        self.config = getJson("config.json")

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.config["ip"],self.config["port"]))
        self.serverSocket.listen(self.config["maxConnections"])

        global connectionDic 
        connectionDic = {}
    
    def acceptConenctions(self):
        while True:
            connection, address = self.serverSocket.accept()

            possibleCodeName = connection.recv(5000)
            possibleCodeName = possibleCodeName.decode()
            print(f"Connection made! IP:{address} Codename {possibleCodeName}")

            try:
                possibleCodeName = possibleCodeName.split(":")
                possibleCodeName[1] == possibleCodeName[1] 
            except Exception as e:
                connection.send(f"{e}".encode())
                connection.close()
            if possibleCodeName[1] == "codename":
                connectionDic[str(possibleCodeName[0])] = [connection,address[0]]
                listenThread = threading.Thread(target=listenToClients,args=[possibleCodeName[0],True])
                listenThread.start()
            else:
                connection.send("Send segistration packet (YOURCODENAME:codename)".encode())
                connection.close()

if __name__ == "__main__":
    serverVar = server()
    acceptThread = threading.Thread(target=serverVar.acceptConenctions)
    acceptThread.start()