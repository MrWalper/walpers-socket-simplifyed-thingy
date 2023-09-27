import socket

def server_program():
    # get the hostname
    host = "localhost"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

class server():
    def __init__(self,maxNum:int, host:str, port:int):
        self.maxNum = maxNum
        self.host = host
        self.port = port

        self.serverSocket = socket.socket()
        self.serverSocket.bind((self.host,self.port))
        self.serverSocket.listen(maxNum)
        self.connection, self.clientAddress = self.serverSocket.accept()
        self.connSet = set()
        self.connList = []
    
    def listenForConnections(self):
        self.conn, self.addr = self.serverSocket.accept()
        if self.conn in self.connSet and self.addr in self.connSet:
            self.connList.append({
                "connection":self.conn,
                "addr":self.addr
            })
    
    def listenToClient(self, logPackets:bool):
        self.data = self.connection.recv(self.port)
        if logPackets:
            print(self.data)
        return self.data

    def sendToClient(self, message:str,connNum:int):
        self.connList[connNum]["connection"].send(message.encode())


#if __name__ == '__main__':
    #server_program()

server = server(maxNum=2,host="localhost",port=5000)

while True:
    server.listenForConnections()
    data = server.listenToClient(True)
    clientNum = input("Num> ")
    msg = input("> ")
    server.sendToClient(message=msg,connNum=clientNum)