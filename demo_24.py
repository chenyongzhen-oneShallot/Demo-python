#coding=utf-8
#客户端
import socket

c=socket.socket()
host=socket.gethostname()
port=12345

c.connect((host,port))
print (c.recv(1024))
c.close()