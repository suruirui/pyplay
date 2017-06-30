# -*- coding=utf-8 -*-
#如果代码中有中文 要声明编码
# print("你好倩倩");
print("hello world");
'''多行注释'''

age = 18 #定义一个变量
print("your age is:%d"%age)
#if判断
if age>=18:
	print("you can goto wangba")

high = int(input("请输入你的身高"))
print("你的身高是:%d"%high)
#输出多个变量
name = "lisi"
print ("i am%s,%d years old,i am%d cm"%(name,age,high))
#if else判断
if high>=180:
	print("you are tall")
# elseif high>=170 && high <180:
# 	print("you are ok")
else:
	print("you are little")



