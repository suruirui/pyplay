# -*- coding:utf-8 -*-

#工厂模式
class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self, carType):
        return self.factory.selectCar(carType)


class Factory(object):
    def selectCar(self, carType):
        if carType == '索纳塔':
            return Suonata()
        elif carType == '名图':
            return Mingtu()
        elif carType == '途胜':
            return Tucson()
        else:
            print("无现车...")


class Car(object):
    def move(self):
        print("move...")

    def play(self):
        print("play music...")


class Suonata(Car):
    pass


class Mingtu(Car):
    pass


class Tucson(Car):
    pass


ssss = CarStore()  #初始化工厂类
s90 = ssss.order("途胜")
s90.move()
