#coding=utf-8
import mysql.connector

#打开数据库连接
try:
    conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="root",database="mydb")

except mysql.connector.Error as e:
  print('connect fails!{}'.format(e))
#使用cursor()方法获取操作游标
cur=conn.cursor()

# 使用execute方法执行SQL语句
#创建user表:
#sql_create="create table mydb.user (id varchar(20) PRIMARY key ,name VARCHAR (20))"
#cur.execute(sql_create)

# 插入一行记录，注意MySQL的占位符是%s:
sql_insert="insert into mydb.user (id,name) values (2,'小张')"
cur.execute(sql_insert)

#数据库查询
sql_select="select *from mydb.user"
cur.execute(sql_select)

# 获取所有记录列表
results=cur.fetchall()
for r in results:
    print r


# 关闭数据库
conn.close()