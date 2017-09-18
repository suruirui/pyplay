#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-18 19:23:34
# @Author  : foxz ()
# @Link    : 
# @Version : $Id$

colors = ['red','blue','green','yellow']
print(colors[0])

print('*******************************')
for c in colors:
	print(c)

print('*******************************')
length = len(colors)
i = 0
while(i<length):
	print(colors[i])
	i+=1
print('*******************************')
colors.append('pink')
for c in colors:
	print(c)
print('*******************************')

nums = [33,2,43,18,30]
nums.sort(reverse=True)
# nums.reverse()
print(nums)

print('asd')

