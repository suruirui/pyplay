# -*- coding:utf-8 -*-

#实现类、创建对象
#人
class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name

#枪
class Gun(object):
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name   #枪名

#弹夹
class Clip(object):
    def __init__(self,maxNum):
        super(Clip,self).__init__()
        self.maxNum = maxNum;

#子弹
class Bullet(object):
    def __init__(self, power):
        super(Bullet, self).__init__()
        self.power = power
        #杀伤力


def main():
    #1.创建老王对象
    laowang = Person("老王")
    #2.创建一个枪对象
    ak47 = Gun("AK47")
    #3.创建一个弹夹对象
    clip = Clip(20)
    #4.创建一些子弹
    bullet = Bullet(10)
    #5.老王把子弹安装到弹夹中

if __name__ == '__main__':
    main()
