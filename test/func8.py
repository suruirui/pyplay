# -*- coding:utf-8 -*-


#不定长参数
def test(a,b,c=33,*args,**kwargs): # *,**用来表示后面的变量有特殊功能
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

A = (44,55,66)
B = {"name":"laowang","age":18}

test(11,22,33,*A,**B) #在实参中，* **表示对元祖/字典进行拆包
