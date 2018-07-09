#coding=utf-8
class Student():
    def __init__(self,name,sorce):
        self.__name=name
        self.__sorce=sorce

    def set_name(self,name):
        self.__name=name

    def set_sorcce(self,sorce):
        self.__sorce=sorce

    def get_name(self):
        return self.__name

    def get_sorce(self):
        return self.__sorce

    def get_grade(self):
        if self.__sorce > 90:
            return '优秀'
        elif self.__sorce >= 60:
            return '及格'
        else:
            return '不及格'

student=Student('小红',100)
print(student.get_grade())
