#coding=utf-8
bob=["Bob Smith",40000]
sue=["Sue jons",30000]
people=[bob,sue]
#切片函数，以空格为分隔符，分割2次，并输出最后一片
#bobName=bob[0].split(" ",1)[-1]
for person in people:
    print person[0].split()[-1]
people.append(["tom",35000])
print people
name,pay=range(2)
print bob[name]