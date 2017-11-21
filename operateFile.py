#coding=utf-8

f=open("file","r")
f_read=f.read()#read是逐字符地读取,read可以指定参数，设定需要读取多少字符，无论一个英文字母还是一个汉字都是一个字符。
print f_read
f.close()

f1=open("file1","w")
f1_write=f1.write("hello,world")
print f1_write
f1.close()

f1=open("file1","a")#与w模式不同的是，a模式不会把原来内容清空，而是光标移到内容最后位置，继续写入新内容。比如在最后追加'hello python'
f1_write=f1.write("\nhello,python")
print f1_write
f1.close()