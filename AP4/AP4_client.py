from socket import *
from cryptography.fernet import Fernet
serverName = 'localhost'
serverPort = 12000
KDCPort = 14000
Alicekey = "1zkOwMr7RRomU_Pka7OCFccOghuToC_zfKgfOKGqKgg="
cipher_suite = Fernet(Alicekey)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,KDCPort))
clientSocket_bob = socket(AF_INET, SOCK_STREAM)
clientSocket_bob.connect((serverName,serverPort))
sentence = "Alice Talking to Bob"
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
nonce = Fernet.generate_key()
clientSocket.send(nonce)
SessionInfo = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
Plaintext_SessionInfo = cipher_suite.decrypt(SessionInfo)
InfoArray = Plaintext_SessionInfo.split(',')
if(InfoArray[0] == nonce):
    print "Data valid. Nonce correct"
    SessionKey = InfoArray[1]
    BobKey = InfoArray[2]
    print "Bob's key: "+BobKey    
    print "Session Key: "+SessionKey   
    print "Sending Data to Bob"
    cipher_suite_Bob = Fernet(BobKey)
    enc_req = cipher_suite_Bob.encrypt(SessionKey)
    clientSocket_bob.send("Alice IP: 10.0.0.6")
    Enc_nonce = clientSocket_bob.recv(1024)
    clientSocket_bob.send(enc_req)
    Enc_nonce = clientSocket_bob.recv(1024)
    cipher_suite_Session = Fernet(SessionKey)
    Bob_nonce = cipher_suite_Session.decrypt(Enc_nonce)
    Bob_nonce = Bob_nonce + '1'
    Bob_nonce_enc = cipher_suite_Session.encrypt(Bob_nonce)
    clientSocket_bob.send(Bob_nonce_enc)
    dat = clientSocket_bob.recv(1024)
    print dat

#key = "1zkOwMr7RRomU_Pka7OCFccOghuToC_zfKgfOKGqKgg="
#cipher_text = cipher_suite.encrypt(b"Password")
#plain_text = cipher_suite.decrypt(cipher_text)
#clientSocket.send(cipher_text)
#print plain_text
clientSocket.close()
