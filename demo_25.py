#coding=utf-8
#多线程
import thread
import time

#Python中使用线程有两种方式：函数或者用类来包装线程对象
#函数式：调用thread模块中的start_new_thread()函数来产生新线程

#新建线程函数
def show_time(threadName,num):
    count=0
    while count<10:
        time.sleep(num)
        count+=1
        print ("%s:%s"%(threadName,time.ctime(time.time())))


#创建2个线程
try:
    thread.start_new_thread(show_time,("thread1",2))
    thread.start_new_thread(show_time,("thread2",2))
except:
    print "Error: unable to start thread"


while 1:
    pass