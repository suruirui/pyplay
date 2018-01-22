#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 11:29:06
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

class Animal:
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name

	def printName(self):  #self指向当前对象的引用
		print('名字为:%s'%self.name)


#定义一个函数
def myPrint(animal):
	animal.printName()

cat = Animal('西西')
myPrint(cat)

cat2 = Animal('北北')
myPrint(cat2)


		
