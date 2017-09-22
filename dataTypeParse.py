#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-21 18:34:13
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

# int() long(x [,base ]) float(x )  转换为一个整数 转换为一个长整数  转换到一个浮点数
# complex(real [,imag ])  创建一个复数
# str(x ) 对象 x 转换为字符串 
# repr(x )  对象 x 转换为表达式字符串
# eval(str ) 在字符串中的有效Python表达式,并返回一个对象
#  tuple(s ) 序列 s 转换为一个元组
# list(s ) 序列 s 转换为一个列表 
# chr(x )整数转换为一个字符 
# unichr(x ) 整数转换为Unicode字符 ord(x )字符转整数值  hex(x )16进制  oct(x )8进制

print(int('2'))
print(long('221314213421'))
print(float('2.2'))

print(str(2))
print(repr(2))
print(eval('2+2')) #4
print(tuple('2+2'))  #('2', '+', '2')
print(list('2+2'))  #['2', '+', '2']
print(list('hello'))  #['h', 'e', 'l', 'l', 'o']
print(chr(55))
print(unichr(2))
print(ord('A')) 
print(hex(2))
print(oct(22))


