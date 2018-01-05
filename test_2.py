#coding=utf-8

bob={'name':'bob','age':40,'pay':10000}
smith={'name':'smith','age':45,'pay':20000}

db={}
db['bob']=bob
db['smith']=smith

if __name__=='__main__':
    for key in db:
        print key,'=>',db[key]

