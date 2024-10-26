import os
import socket 
from Crypto.Cipher import AES  


HOST = 'localhost'
PORT = 9090
key = b'NorthLondonfrvar'
nonce = b'NorthLondonfreva'
cipher = AES.new(key,AES.MODE_EAX,nonce)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))


with open('img.pdf','rb') as f:
    data = f.read()
encrypted = cipher.encrypt(data)
file_size= os.path.getsize('img.pdf')
client.send('recieved_img.pdf'.encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b'<END>')
client.close()
    