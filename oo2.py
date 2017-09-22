#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 11:01:39
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

class Car(object):
	"""docstring for Car"""
	def __init__(self, newWheelNum,newColor):
		super(Car, self).__init__()
		self.wheelNum = newWheelNum
		self.color = newColor

	def __str__(self):
		msg = "嘿。。。我的颜色是" + self.color + "我有" + str(self.wheelNum) + "个轮胎..."
		return msg

	def move(self):
		print('car start...')

audiA6 = Car(4,'白色')
print('audiA6的车轮个数:%d,颜色是:%s'%(audiA6.wheelNum,audiA6.color))
volvoxc90 = Car(5,'青色')
print('volvoxc90的车轮个数:%d,颜色是:%s'%(volvoxc90.wheelNum,volvoxc90.color))
#当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
print(audiA6)
print(volvoxc90)


class Person(object):
	"""docstring for Person"""
	def __init__(self, nName,nAge):
		super(Person, self).__init__()
		self.name = nName
		self.age = nAge

	def run(self):
		print("i am %s,i'm %d years old,i can run fast..."%(self.name,self.age))


tom = Person('Jack',22)
print('tom的名字是：%s'%tom.name)
print('tom的年龄是：%d'%tom.age)
tom.run()

