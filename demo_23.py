#coding=utf-8
#服务端
import socket

s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))

s.listen(5)
while True:
    c,addr=s.accept()
    print("链接地址：",addr)
    c.send("hello world")
    c.close()
