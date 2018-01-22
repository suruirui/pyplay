#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-12
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

#定义类
class Car(object):
	def __init__(self):
		super(Car,self).__init__()
		self.wheelNum = 4
		self.color = '蓝色'

	def start(self):
		print("start")

c = Car();	
print('车的轮子个数为%s'%c.wheelNum);
print('车的颜色为%s'%c.color);
