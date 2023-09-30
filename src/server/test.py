import socket
import threading

# Define the server IP address and port
SERVER_IP = 'localhost'  # Listen on all available network interfaces
SERVER_PORT = 5000

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(2)  # Allow up to 2 clients to connect at a time

# List to store client connections and IPs

def handle_client(client_socket, client_ip):
    try:
        # Send a welcome message to the client
        client_socket.send(b"Welcome to the server!")

    except Exception as e:
        print(f"Error handling client: {e}")
    while True:
        try:
            print(client_socket.recv(5000))
        except Exception as e:
            print(e)

print("Server is listening for connections...")

clientDic = {}

def acceptConenctions():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address[0]))
        client_handler.start()
        clientDic[client_address] = client_socket
        try:
            print(client_socket.recv(5000))
        except Exception as e:
            print(e)

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    clientDic[client_address[0]] = client_socket
    clientDic[client_address[0]].send(b"Test message")
    print(client_address[0])
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address[0]))
    client_handler.start()
    #clientListener = threading.Thread(target=client_socket.recv,args=5000)
    #clientListener.start()


    