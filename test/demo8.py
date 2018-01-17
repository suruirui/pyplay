# -*- coding:utf-8 -*-

#隐藏对象的属性 -属性私有
class Dog:
    def __init__(self,name):
        self.name = name
        self.__age = 0  #定义了一个私有的属性,属性的名字是__age

    def setAge(self, age):
        if age > 0 and age <= 100:
            self.__age = age
        else:
            self.__age = 0

    def getAge(self):
        return self.__age


dog = Dog("猪胖")

dog.setAge(-10)
age = dog.getAge()
print(age)
#以下方法仍可以读写公有属性
# dog.age = -10
# print(dog.age)  #无法读取私有属性

print(dog.__age)  #'Dog' object has no attribute '__age' 私有属性无法访问