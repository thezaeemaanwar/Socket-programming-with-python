# Import socket module
import socket
import sys

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(("127.0.0.1", port))

clientFile = open("InfoClient.txt", "wb")

fromServer = s.recv(1024)
clientFile.write(fromServer)

print("File recieved from the server and saved as InfoClient.txt")
s.close()
