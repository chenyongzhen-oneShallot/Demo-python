#coding=utf-8
from test_2 import db
import pickle
dbfile=open('user','wb')
pickle.dump(db,dbfile)
dbfile.close()

