# -*- coding:utf-8 -*-

class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None  #用来保存枪对象的引用
        self.hp =100

    #把子弹装到弹夹中
    def addBullet(self,clip,bullet):
        clip.addB(bullet)

    #把弹夹放入枪中
    def addClip(self,gun,clip):
        gun.addC(clip)

    #拿枪
    def takeGun(self, gun):
        self.gun = gun

    def __str__(self):
        if self.gun:
            return "%s的血量为:%d, 他有枪 %s" % (self.name, self.hp, self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为%d, 他没有枪" % (self.name, self.hp)
            else:
                return "%s 已挂...." % self.name

    def launch(self, enemy):  #开枪
        self.gun.fire(enemy)

    def drainBlood(self, power):  #掉血
        self.hp -= power


class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        self.clip = None  #用来记录弹夹对象的引用

    #插入弹夹
    def addC(self, clip):
        self.clip = clip

    #开火
    def fire(self, enemy):
        bullet = self.clip.shoot()
        if bullet:
            bullet.hit(enemy)
        else:
            print("弹夹中没有子弹了")

    def __str__(self):
        if self.clip:
            return "枪的信息为:%s, %s" % (self.name, self.clip)
        else:
            return "枪的信息为:%s, 这把枪中没有弹夹" % (self.name)


#弹夹
class Clip(object):
    def __init__(self, maxNum):
        super(Clip, self).__init__()
        self.maxNum = maxNum  #弹夹最大容量
        self.bulletList = []  #所有子弹的引用

    def addB(self, bullet):
        self.bulletList.append(bullet)

    def shoot(self):  #射击弹出最上面的那颗子弹
        if self.bulletList:
            return self.bulletList.pop()
        else:
            return None

    def __str__(self):
        return "弹夹的信息为:%d/%d" % (len(self.bulletList), self.maxNum)


#子弹类
class Bullet(object):
    def __init__(self, power):
        super(Bullet, self).__init__()
        self.power = power  #子弹的威力

    def hit(self, enemy):
        #敌人.掉血(一颗子弹的威力)
        enemy.drainBlood(self.power)


def main():
    laowang = Person("老王")  #创建老王对象
    ak47 = Gun("ak47")  #创建一个枪对象
    clip = Clip(20)  #创建一个弹夹对象
    #创建一些子弹
    for i in range(15):
        bullet = Bullet(10) #创建威力系数为10的子弹
        laowang.addBullet(clip, bullet)  #老王把子弹安装到弹夹中

    laowang.addClip(ak47, clip)  #老王把弹夹安装到枪中
    #测试枪和弹夹
    print(clip)
    print(ak47)

    laowang.takeGun(ak47)  #抄家伙

    print(laowang)

    enemy = Person("小炮")  #创建敌人
    print(enemy)

    #开枪
    print("——————————————————开打——————————————————")
    laowang.launch(enemy)
    print(enemy)
    print(laowang)
    laowang.launch(enemy)
    print(enemy)
    print(laowang)
    laowang.launch(enemy)
    print(enemy)
    print(laowang)
    
   


if __name__ == '__main__':
    main()
