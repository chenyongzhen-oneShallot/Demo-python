#coding=utf-8

#继承
class parent:

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print "调用父类方法"


class child(parent):

    def __init__(self):
        print "调用子类构造函数"

    def childMethod(self):
        print "调用子类方法"

object=child()
object.parentMethod()
object.childMethod()