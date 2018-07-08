#coding=utf-8
list=['hello','world',25,'nice']
for i in list:
    if isinstance(i,str):
        print(i,'是字符串')
    else:
        print(i,'不是字符串')

print([i for i in list if isinstance(i,str)])