# -*- coding:utf-8 -*-

# 杂项
# 函数的文档说明


def test():
    """这是用来完成xxx功能的"""
    print("asdfasdaafasfa")


#交换两个值
a = 10
b = 100

a, b = b, a

print("a=%d,b=%d" % (a, b))

#指向
a = [100]

def demo(num):
    #num += num #+=表示 num指向谁就对谁进行修改,如果num指向[100],那么就变为[100,100]
    #如果num 指向100,因为100是不可变类型,所以不能修改,所以num=num+num
    num = num + num #===>[100] + [100] ====>[100,100]   注意只要是num=xxx一定是num指向了一个新的地方
    print(num)

demo(a)
print(a)
