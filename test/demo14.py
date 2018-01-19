# -*- coding:utf-8 -*-

#只初始化1次

class Dog(object):

    __instance = None
    __initFlag = False

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return  cls.__instance
        else:
            return cls.__instance

    def __init__(self,name):
        if Dog.__initFlag == False:
            self.name = name
            Dog.__initFlag = True

a = Dog("zhupang")
print(id(a))
print(a.name)

b = Dog("erha")
print(id(b))
print(b.name)