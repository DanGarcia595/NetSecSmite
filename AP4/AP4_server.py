from socket import *
from cryptography.fernet import Fernet
import sys
key = "LJzbk-Uq63uhhcX5m76PtsvFTpqo_O5boM5112cEmG8="
cipher_suite = Fernet(key)
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Who are you?'
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print sentence
    if(sentence == "Alice IP: 10.0.0.6"):
        print "I got something"
        connectionSocket.send("Start Session.")
        Session = connectionSocket.recv(1024)
        SessionKey = cipher_suite.decrypt(Session)
        nonce = Fernet.generate_key()
        cipher_suite_Session = Fernet(SessionKey)
        Enc_nonce = cipher_suite_Session.encrypt(nonce)
        connectionSocket.send(Enc_nonce)
        Enc_Iterated_nonce = connectionSocket.recv(1024)
        Iterated_nonce = cipher_suite_Session.decrypt(Enc_Iterated_nonce)
        if(Iterated_nonce == nonce + '1'):
            print "Nonce verified. Alice Alive. Authentication Correct"
            connectionSocket.send("Welcome, Alice")
connectionSocket.close()
