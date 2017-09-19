#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-19 19:35:23
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$
# 元组的使用 （）
#元组与列表类似，不同之处在于元组的元素不能修改和删除
aTuple = ('et',77,99.9)
print(aTuple)
print(aTuple[0])
print(aTuple[1])
print(aTuple[2])
#index count用法与字符串相似
att = ('a', 'b', 'c', 'a', 'b')
print(att.index('a', 1, 4)) # 注意是左闭右开区间  3
#IndentationError：unexpected indent  错误的使用缩进量
print(att.count('b'))




