# -*- coding:utf-8 -*-

#定义类
class Cat:

    """定义一个Cat类"""
    #初始化对象 __init__方法
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #__str__方法
    def __str__(self):
        return "%s的年龄是:%d岁"%(self.name,self.age)

    #方法
    def eat(self):
        print("%s在吃鱼..."%self.name)

    def catchMouse(self):
        print("%s第一次抓老鼠是在%d岁的时候"%(self.name,self.age))

#创建对象
xigua = Cat("西瓜",2)

xigua.eat()
xigua.catchMouse()

tom = Cat("Tom",3)
tom.eat()
tom.catchMouse()

print(tom)      #如果没有__str__方法 打印对象会输出地址值 否则调用__str__方法
print(xigua)