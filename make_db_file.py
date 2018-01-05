#coding=utf-8
#把db保存到user中
from test_2 import db
import pickle
dbfile=open('user','wb')
pickle.dump(db,dbfile)
dbfile.close()

