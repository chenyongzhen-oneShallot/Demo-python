#coding=utf-8
list=range(1,10)
print([x*x for x in list])

list1=['A','B','C']
list2=['X','Y','Z']
print([m+n for m in list1 for n in list2])

print([x*x for x in list if x%2==0] )