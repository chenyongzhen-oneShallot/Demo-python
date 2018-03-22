#coding=utf-8
class employee:
    #构造函数，当创建对象时调用该函数
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone

    def displayName(self):
        print self.name

em1=employee('bob',20,13500000000)#这一步调用构造函数
em1.displayName()


