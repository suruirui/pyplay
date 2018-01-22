# -*- coding:utf-8 -*-

#列表当作全局变量
nums = {11,22,33}

info = {"name":"laowang"}

def test():
    nums.add(44)
    info['age'] =18 

def test2():
    print(nums)
    print(info)

test()
test2()