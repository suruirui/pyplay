#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-21 19:34:07
# @Author  : foxz (wc332431830@163.com)
# @Link    : suruirui.github.io
# @Version : $Id$

def add(a,b):
	return a+b
print(add(2,3))

def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end----')


def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')

testA()
