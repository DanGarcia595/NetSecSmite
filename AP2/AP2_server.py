from socket import *
import sys
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Who are you?'
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    if(sentence == "Alice IP: 10.0.0.6"):
        print "I got something"
        connectionSocket.send("Welcome, Alice")
    connectionSocket.close()
