#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 10:50:20
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

#定义类
class Car(object):
	"""docstring for Car"""
	#__init__初始化函数，用来完成一些默认的设定
	def __init__(self):
		super(Car, self).__init__()
		self.wheelNum = 4
		self.color = '蓝色'

	def move(self):
		print('car start...')
#创建对象
bmw = Car() #没有New关键字!!!!
print('车的颜色为:%s'%bmw.color)
print('车轮胎数量为:%d'%bmw.wheelNum)

