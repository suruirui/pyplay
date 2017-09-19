#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-19 19:21:39
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$
#一个列表中的元素又是一个列表，那么这就是列表的嵌套
#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
import random
# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0

for name in names:
	index = random.randint(0,2)
	offices[index].append(name)

i = 1
for tempNames in offices:
	print('办公室%d的人数为:%d'%(i,len(tempNames)))
	i+=1
	for name in tempNames:
		print('%s'%name)
	print('\n')
	print('-'*20)
