# -*- coding:utf-8 -*-

class CarStore(object):
    def order(self, money):
        if money > 50000:
            return Car()

class Car(object):
    def move(self):
        print("车在移动....")

    def playMusic(self):
        print("播放音乐...")

    def stop(self):
        print("车在停止")

carStore = CarStore()
car = carStore.order(100000)
car.move()
car.playMusic()
car.stop()
