#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#第三方SMTP服务
mail_host="smtp.163.com"  #设置服务器,要在个人邮箱设置里面开启smtp服务
mail_user="cyz891354032@163.com" #用户名
mail_password="cyz1990123"  #密码

sender="cyz891354032@163.com"
receiver="891354032@qq.com"

message=MIMEText("hello baby","plain","utf-8")
message["From"]="cyz891354032@163.com"
message["To"]="891354032@qq.com"
subject="hello baby"
message["Subject"]=Header(subject,"utf-8")


try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_password)
    smtpObj.sendmail(sender,receiver,message.as_string())
    smtpObj.quit()
    print "发送成功"
except smtplib.SMTPException:
    print "Error:发送失败"



