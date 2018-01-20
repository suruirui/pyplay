# -*- coding:utf-8 -*-

#如果导入这个模块的方式是 from 模块名 import * ,那么仅仅会导入__all__的列表中包含的名字
__all__ = ['test1','test']

def test1():
    print("---test1---")

def test2():
    print("---test2---")

num = 100

class Test(object):
    pass