#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-19 19:46:52
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

#字典(键值对)

info = {'name':'lisi','age':20,'gender':'男','addr':'北京'}

#若访问不存在的键，则会报错,可以使用get方法来访问，若键不存在返回None
print(info['name'])
print(info['age'])
print(info['addr']) 

gender = info.get('xxx')  #None
print(gender)

#修改字典
info['age'] = 22
#添加元素
info['id'] = 1
#删除元素
del info['id'] 

#字典中键值对的个数
print('info键值对个数为%d'%len(info))
#keys()拿到所有key的列表
print(info.keys())
#values()拿到所有value的列表
print(info.values())
#items返回包含所有键值对元组的列表
print(info.items())
#has_key检测是否包含key
print(info.has_key('id'))
for key in info:
	val = info[key]
	print("%s-----%s"%(key,val))


for item in info.items():
	print(item)

for key,value in info.items():
	print('key=%s,value=%s'%(key,value))
# del info #删除整个字典 name 'info' is not defined
#清空字典
info.clear()

print(info) 


