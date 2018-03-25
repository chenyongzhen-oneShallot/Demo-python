#coding=utf-8
#类的私有属性

class people:
    __count=1
    num=10

    def display_count(self):
        print(self.__count)

    def display_num(self):
        print(self.num)

bob=people()
bob.display_count()
bob.display_num()
print(bob.num)

#__count是私有变量，类之外的不能访问
#print(bob.__count)
