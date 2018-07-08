#coding=utf-8
import time
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))

now()