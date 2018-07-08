#coding=utf-8
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=12347
s.connect((host,port))
#每次最多接受1K字节
print (s.recv(1024))
s.close()