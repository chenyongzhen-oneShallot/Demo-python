#coding=utf-8
#获取当前时间戳
import time
import calendar
print(time.time())

#h获取当前时间
print(time.localtime(time.time()))

#获取格式化时间
print(time.asctime(time.localtime(time.time())))

#格式化日期
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

#获取日历
print(calendar.month(2018,3))