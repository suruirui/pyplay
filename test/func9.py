# -*- coding:utf-8 -*-

#递归 求阶乘
def getNums(num):
    if num > 1:
        return num * getNums(num - 1)
    else:
        return num 

result = getNums(10)
print(result)
