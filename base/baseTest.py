#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-21 19:05:37
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

#对一个元素全为数字的列表，求最大值、最小值
nums = [11,3,4,12,323,2]

maxMin = 0
i = 0
j = 0
while(i<len(nums)):
	if(nums[i] > maxMin):
		maxMin = nums[i]
	# print nums[i]
	i+=1

print '列表nums最大值为：%d'%maxMin
while(j<len(nums)):
	if(nums[j] < maxMin):
		maxMin = nums[j]
	j+=1
print '列表nums最小值为：%d'%maxMin

# 统计字符串中，各个字符的个数
# 比如："hello world" 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1

str = 'hello world'
dict = {}
for s in str:
	if(s <> ' '):
		# print s
		if(s not in dict):
			dict[s] = 1
		else:
			dict[s] +=1
print(dict)

#完成一个路径的组装
# 先提示用户多次输入路径，最后显示一个完整的路径，比如/home/python/ftp/share
pathName = input('请输入路径:')
print pathName



'''
完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
'''
