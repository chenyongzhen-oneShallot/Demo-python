#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#第三方SMTP服务
mail_host="smtp.163.com"  #设置服务器
mail_user="cyz891354032@163.com" #用户名
mail_password="cyz1990123"  #密码

sender="91354032@163.com"
receiver="891354032@qq.com"

message=MIMEText("python发送邮件测试","text","utf-8")
message["From"]=Header("cyz891354032","utf-8")
message["To"]=Header("迷途小书童_臻","utf-8")
subject="SMTP邮件测试"
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
