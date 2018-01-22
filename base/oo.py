#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-22 10:41:28
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

class Car:
	def move(self):
		print('car start...')

	def toot(self):
		print('car toot...')


bmw = Car()
bmw.color = '黑色';
bmw.brand = '宝马';
print(bmw.color)
print(bmw.brand)
bmw.move()
bmw.toot()