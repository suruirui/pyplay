# -*- coding:utf-8 -*-

class CarStore(object):
    def order(self,carType):
        if carType == '索纳塔':
            return Suonata()
        elif carType == '名图':
            return Mingtu()


class Car(object):
    def move(self):
        print("点火启动...")
    def playMusic(self):
        print("播放音乐...")
    def stop(self):
        print("刹车....")

class Suonata(Car):
    pass  #pass空操作

class Mingtu(Car):
    pass