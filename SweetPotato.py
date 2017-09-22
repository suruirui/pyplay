#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 11:35:10
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$
#定义地瓜类
class SweetPotato:
	"""docstring for SweetPotato"""
	#定义初始化方法
	def __init__(self):  
		self.cookedLevel = 0
		self.cookedString = '生的'
		self.condiments = []

	#定制print时的显示内容
    def __str__(self):
        msg = self.cookedString + " 地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("

            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg = msg + ")"
        return msg


	def cook(self,time):
		self.cookedLevel += time
		if self.cookedLevel > 8:
			self.cookedString = '烤成灰了'
		elif self.cookedLevel > 5:
			self.cookedString = '烤好了'
		elif self.cookedLevel > 3:
			self.cookedString = '半生不熟'
		else:
			self.cookedString = '生的'

	#添加配料
	def addCondiments(self, myCondiments):
        self.condiments.append(myCondiments)


mySweetPotato = SweetPotato()
mySweetPotato.cook(6) #烤4分钟
# mySweetPotato.addCondiments('番茄酱')

# print(mySweetPotato.cookedLevel)
# print(mySweetPotato.cookedString)
# print(mySweetPotato.condiments)

print(mySweetPotato)
