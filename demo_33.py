#coding=utf-8
class Student():
    def __init__(self,name,sorce):
        self.name=name
        self.sorce=sorce

    def get_grade(self):
        if self.sorce>90:
            return '优秀'
        elif self.sorce>=60:
            return '及格'
        else:
            return '不及格'

chenyz=Student('小明',100)
print(chenyz.get_grade())
print(chenyz.name)


