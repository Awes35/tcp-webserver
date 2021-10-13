from socket import *
import sys
import argparse

#Create a TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#get the address, port, and the page client wishes to access
address = str(input("input the IP Address: "))
port = int(input("input the Port Number: "))
fileName = str(input("input page you want to access(ex: HelloWorld.html): "))

#create the Get Request on HTTP 1.1
getRequest = "GET /" + fileName + " HTTP/1.1\r\n\r\nHost: 192.168.188.128\n\n"

#initialize communication with server through TCP socket on give port
clientSocket.connect((address, port))
#send Get Request for specific page
clientSocket.send(getRequest.encode())

#receive respose from server and build the message to print
message = clientSocket.recv(4096).decode()
result = message
while (len(message) > 0):
    message = clientSocket.recv(4096).decode()
    result = result + message

print(result)
clientSocket.close()
