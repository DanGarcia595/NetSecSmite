from socket import *
from cryptography.fernet import Fernet
import sys
Alicekey = "1zkOwMr7RRomU_Pka7OCFccOghuToC_zfKgfOKGqKgg="
BobKey = "LJzbk-Uq63uhhcX5m76PtsvFTpqo_O5boM5112cEmG8="
SessionKey = Fernet.generate_key()
cipher_suite = Fernet(Alicekey)
serverPort = 14000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Who needs a key?'
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    if(sentence == "Alice Talking to Bob"):
        connectionSocket.send("Nonce needed")
        Nonce = connectionSocket.recv(1024)
        reply = Nonce + "," + SessionKey + "," + BobKey
        Enc_reply = cipher_suite.encrypt(reply)
        connectionSocket.send(Enc_reply)
connectionSocket.close()
