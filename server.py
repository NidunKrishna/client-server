import os
import socket 
from Crypto.Cipher import AES  
HOST = 'localhost'
PORT = 9090 
key = b'NorthLondonfrvar'
nonce = b'NorthLondonfreva'
cipher = AES.new(key,AES.MODE_EAX,nonce)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()


client , addr = server.accept()
file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()
file_size = int(file_size)
print(f"the file {file_name} has a sizeof {file_size}")

file = open(file_name, 'wb')
file_bytes = b""
done = False 

while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b'<END>':
        done = True 
    else:
        file_bytes += data
file.write(cipher.decrypt(file_bytes))
print(file_bytes)
file.close()
server.close()
client.close()

        