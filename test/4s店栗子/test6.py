# -*- coding:utf-8 -*-

class Store(object):

    def selectCar(self):
        pass
        
    def order(self, carType):
        return self.selectCar(carType)

class BMWStore(Store):
    def selectCar(self,carType):
        return BMWFactory().selectCar(carType)

class BMWFactory(object):
    def selectCar(self,carType):
        if carType == 'x1':
            return X1()
        elif carType == 'x3':
            return X3()
        elif carType == 'x5':
            return X5()

class Car(object):
    def move(self):
        print("moveing....")
    def playMusic(self):
        print("play music....")
    def stop(self):
        print("刹车……")

class X1(Car):
    pass

class X3(Car):
    pass

class X5(Car):
    pass

