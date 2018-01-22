# -*- coding:utf-8 -*-

#定义人类 老王/敌人
class Person(object):
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None  #记录持枪对象的引用
        self.hp = 100

    #装子弹到弹夹中
    def addBullet(self,clip,bullet):
        clip.addB(bullet)

    #把弹夹放入枪中
    def addClip(self,gun,clip):
        gun.addC(clip)

    #拿枪
    def takeGun(self,gun):
        self.gun = gun

    #开枪
    def launch(self, enemy):
        self.gun.fire(enemy)

    #掉血
    def drainBlood(self, power):
        self.hp -= power

    def __str__(self):
        if self.gun:
            return "%s的血量为:%d,他有枪%s,"%(self.name,self.hp,self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为:%d,他没有枪"%(self.name,self.hp)
            else:
                return "%s已挂...."%self.name

#枪类
class Gun(object):
    def __init__(self,name):
        super(Gun,self).__init__()
        self.name = name
        self.clip = None  #记录弹夹对象的引用

    #插入弹夹
    def addC(self,clip):
        self.clip = clip

    #开火
    def fire(self,enemy):
        bullet = self.clip.shoot()
        if bullet:
            bullet.hit(enemy)
        else:
            print("弹夹中没有子弹了")

    def __str__(self):
        if self.clip:
            return "枪的信息为:%s,%s"%(self.name,self.clip)
        else:
            return "枪的信息为%s,这把枪中没有弹夹"%(self.name)

#弹夹对象
class Clip(object):
    def __init__(self,maxNum):
        super(Clip,self).__init__()
        self.maxNum = maxNum  #弹夹最大容量
        self.bulletList = []  #所有子弹的引用

    def addB(self,bullet):
        self.bulletList.append(bullet)

    def shoot(self):
        if self.bulletList:
            return self.bulletList.pop()
        else:
            return None

    def __str__(self):
        return "弹夹的信息为:%d/%d" % (len(self.bulletList), self.maxNum)


#子弹对象
class Bullet(object):
    def __init__(self,power):
        super(Bullet,self).__init__()
        self.power = power #子弹的威力

    #射敌 掉血为一颗子弹的威力
    def hit(self,enemy):
        enemy.drainBlood(self.power)


def main():
    laowang = Person("laowang")
    ak47 = Gun("ak47")
    clip = Clip(20)
    for i in range(15):
        bullet = Bullet(10) #威力系数为10的子弹
        laowang.addBullet(clip, bullet)

    laowang.addClip(ak47,clip) #安装弹夹
    #测试枪和弹夹
    print(clip)
    print(ak47)

    laowang.takeGun(ak47)  #拿枪
    print(laowang)

    enemy = Person("奥巴马")
    print(enemy)

    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)
    print("-----开火-----")   
    laowang.launch(enemy)  #朝敌人开枪
    print(laowang)
    print(enemy)






if __name__ == '__main__':
    main()
