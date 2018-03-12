#coding=utf-8
#if语句
print '请输入您的成绩：'
#raw_input默认输入的是str类型，所以这个地方得强制转换成int型
i=int(raw_input())
if i<60:
    print "不及格"
elif 60<=i<=80:
    print "良好"
else:
    print "优秀"