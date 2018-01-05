#coding=utf-8
import thread
import time

#为线程定义一个函数
def print_time(threadName,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print "%s：%s" % (threadName,time.ctime(time.time()))


#创建两个线程

t1=print_time, ("Thread-1", 2,)
t2=print_time, ("Thread-2", 4,)
thread.t1
thread.t2
