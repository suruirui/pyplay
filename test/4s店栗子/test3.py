# -*- coding:utf-8 -*-

class CarStore(object):
    def order(self,carType):
        if carType=='索纳塔':
            return Suonata()
        elif carType == '名图':
            return Mingtu()
        elif carType == '途胜':
            return Tucson()

class Car(object):
    def move(self):
        print("车在跑...")

    def playMusic(self):
        print("正在播放音乐")

    def stop(self):
        print("刹车...")

class Suonata(Car):
    pass

class Mingtu(Car):
    pass

class Tucson(Car):
    pass


carStore = CarStore()
car = carStore.order("途胜")
car.move()
car.playMusic()
car.stop()