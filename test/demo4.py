# -*- coding:utf-8 -*-

#定义一个类

class Cat:   
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼...")

    def drink(self):
        print("猫在喝水.....")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))

#创建一个对象
tom = Cat()

tom.eat()

tom.drink()

#添加属性
tom.name = "汤姆"
tom.age = 40

#获取对象的属性 方法1
# print("%s的年龄是:%d"%(tom.name,tom.age))

#获取对象的属性 方法2
tom.introduce()

#更多对象
xigua = Cat()

xigua.eat()
xigua.drink()

xigua.name = "西瓜"
xigua.age = 2
xigua.introduce()