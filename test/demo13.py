# -*- coding:utf-8 -*-

#单例模式
class Dog(object):

    __instance = None

    def __new__(cls):
        if cls.__instance == None:
             cls.__instance = object.__new__(cls)
             return cls.__instance
        else:
            return cls.__instance  #return上次创建对象的引用

a = Dog()
print(id(a))

b = Dog()
print(id(b))