#coding=utf-8
import re
#根据正则表达式判断手机号码
phone=raw_input("请输入手机号码：\n")
p2=re.match("^(135)\d{8}$",phone)
if p2:
    print ("您输入的手机号码为："),phone
else:
    print ("您输入的手机号码不合法，请重新输入")