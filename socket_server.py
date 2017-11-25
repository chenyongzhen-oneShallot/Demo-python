#coding=utf-8
import socket
#创建一个socket对象,AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6,SOCK_STREAM指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取本地主机名
host=socket.gethostname()
#设置端口
port=12345
#绑定端口，同一个端口被一个socket绑定后就不会被别的socket绑定了
s.bind((host,port))
#等待客户端链接，参数表示等待链接的最大数量
s.listen(5)
while True:
    #建立客户端链接
    c,addr=s.accept()
    print "链接地址：",addr
    c.send("欢迎访问菜鸟教程")
    c.close()