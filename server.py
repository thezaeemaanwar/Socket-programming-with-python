import socket
import sys

s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(("", port))
print("socket bound to port %s" % (port))

# Accept upto 5 connections
s.listen(5)
print("socket is listening")


file1 = open("Info.txt", "rb")

while True:
    client, addr = s.accept()
    print("client connected from : ", addr)
    file1.seek(0)
    readFile = file1.read(1024)
    while readFile:
        client.send(readFile)
        readFile = file1.read(1024)
    client.close()

s.close()
