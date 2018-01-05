#coding=utf-8
#从test_2.py中读取数据并存到file里面
with open('test_2.py','r') as f1:
    with open('file','w') as f2:
        f2.write(f1.read())