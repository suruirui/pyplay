# -*- coding:utf-8 -*-

#局部变量和全局变量的区别1

#定义一个全局变量 温度
temperature = 0


def getTemperature():
    #如果温度这个变量已经在全局变量的位置定义了，此时还想在函数中对这个全局变量进行修改的话
    #那么 仅仅是 temperature=一个值  这还不够,,,此时temperature这个变量是一个局部变量,仅仅是和全局变量的名字
    #相同罢了
    #temperature = 33

    #使用global用来对一个全局变量的声明 ，那么这个函数中的temperature = 33就不是定义一个局部变量,而是
    #对全局变量进行修改
    global temperature
    temperature = 33


def printTemp():
    print("温度是%d"%temperature)

getTemperature()  #修改了温度
printTemp()
