#coding=utf-8
#从user中读取db
import pickle
dbfile=open('user','rb')
db=pickle.load(dbfile)
for key in db:
    print key,'=>',db[key]