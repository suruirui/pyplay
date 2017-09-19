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
A = [1,2]
B = [3,4]
A.append(B)
print(A)
A.extend(B)
print(A)
print('*******************************')
lang = ['java','js','c']
lang[0] = 'python'
print(lang)
print('*******************************')
#待查找的列表
nameList = ['xiaoWang','xiaoZhang','xiaoHua']
#获取用户要查找的名字
findName = 'xiaoWang'

#查找是否存在
if findName in nameList:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')
print('*******************************')
#插入操作
nums = [1,2,3,4]
nums.insert(1,0)
print(nums)
print('*******************************')
#index  count 
a = ['a', 'b', 'c', 'a', 'b']
# print(a.index('a', 1, 3)) # 注意是左闭右开区间
print(a.index('a', 1, 4))   #3
print(a.count('a'))         #2 
print('*******************************')
#删除元素
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
del movieName[2] #根据下标删除
movieName.pop()  #删除最后一个元素
movieName.remove('指环王')  #根据元素的值进行删除
for movie in movieName:
	print(movie)  

print('*******************************')

nums = [33,2,43,18,30]
nums.sort(reverse=True) #sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小
# nums.reverse()  #reverse方法是将list逆置
print(nums)   



