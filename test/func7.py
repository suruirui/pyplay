# -*- coding:utf-8 -*-

#不定长参数


def sum2Nums(a, b, *args):
    print("-" * 30)
    print("a=%d"%a)
    print("b=%d"%b)
    print(args)

    result = a + b
    for num in args:
        result += num

    print("result=%d" % result)


sum2Nums(11, 22, 33, 44, 55, 66, 77)
sum2Nums(11, 22, 33)
# sum2Nums(11)  #缺少参数
