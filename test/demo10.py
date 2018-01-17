# -*- coding:utf-8 -*-

#继承
class Animal:
    # def __init__(self,name):
    #     self.name = name

    def eat(self):
        # print("%s在吃饭"%self.name)
        print("吃饭")


class Dog(Animal):
    #重写
    def eat(self):
        Animal.eat(self)  #调用被重写的父类的方法1
        print("吃骨头...")

    def lookDoor(self):
        # print("%s看门中..."%self.name)
        print("看门中...")


class Cat(Animal):
    #重写
    def eat(self):
        super().eat()  #调用被重写的父类的方法2
        print("吃鱼...")

    def catchMouse(self):
        # print("%s抓到了老鼠..."%self.name)
        print("抓到了老鼠...")


class Erha(Dog):
    def run(self):
        print("跑")


zhupang = Dog()
zhupang.eat()
zhupang.lookDoor()

xigua = Cat()
xigua.eat()
xigua.catchMouse()

erha = Erha()
erha.eat()
erha.lookDoor()
erha.run()