#coding=utf-8
#更新数据
import pickle
#打开文件
dbfile=open('user','rb')
#把文件内容加载到内存中
db=pickle.load(dbfile)
dbfile.close()

db['bob']['pay']=50000

dbfile=open('user','wb')
pickle.dump(db,dbfile)
dbfile.close()

print db

