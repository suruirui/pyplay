# -*- coding:utf-8 -*-


#定义函数
# 定义名片管理系统
def print_menu():
    print("=" * 50)
    print("名片管理系统v0.1")
    print(" 1:xxx")
    print(" 2:xxx")
    print("=" * 50)


def print_sanjiaoxing():
    print("*")
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)


print_menu()
print_sanjiaoxing()


# 定义带有参数和返回值的的函数
def add(a, b):
    return a + b


c = add(2, 2)
print(c)


# 多个返回值的函数
def test():
    a = 11
    b = 22
    c = 33
    return a,b,c

num = test()
print(num)  #(11, 22, 33)

# 函数的嵌套调用
def sayHello():
    print_menu()
    print_sanjiaoxing()
    print("hello")


sayHello()


#匿名函数
def test1(a,b):
    return a + b

result1 = test1(11,22)

test2 = lambda a, b: a + b  #lambda定义匿名函数

result2 = test2(11, 22)  #调用匿名函数

print("result1=%d,result2=%d" % (result1, result2))

#匿名函数应用
infos = [{"name":"jack","age":10},{"name":"lisi","age":20},{"name":"rose","age":12}]

infos.sort(key = lambda x:x['age'])

print(infos)

def test(a,b,func):
    result = func(a,b)
    return result

num = test(11,22,lambda)


