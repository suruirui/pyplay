# -*- coding:utf-8 -*-

#局部变量和全局变量的区别2


def getTemp():
    temp = 33
    return temp


def printTemp(temp):
    print("温度是%d" % temp)


tmp = getTemp()  #需要调用函数才能取得函数的返回值然后赋值给变量

printTemp(tmp)
