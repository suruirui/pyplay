# -*- coding:utf-8 -*-
#烤地瓜
class SweetPotato:
    """定义了一个地瓜类"""
    def __init__(self):
        self.state = "生的"  #地瓜状态
        self.level = 0       #烤熟等级
        self.condiments = [] #佐料 当属性是列表 可以存储多个数据

    def __str__(self):
        return "地瓜的状态:%s(%d),添加的佐料有:%s"%(self.state,self.level,str(self.condiments))
    #烤的方法
    def grilled(self, time):
        self.level += time
        if self.level >= 0 and self.level < 3:
            self.state = "生的"
        elif self.level >=3 and self.level < 5:
            self.state = "半生不熟"
        elif self.level >=5 and self.level < 8:
            self.state = "熟了"
        elif self.level > 8:
            self.state = "烤糊了"
    #添加佐料
    def addCondiments(self,item):
        self.condiments.append(item)


#创建一个地瓜对象
sweetPotato = SweetPotato()

print(sweetPotato)

#开始烤地瓜
sweetPotato.grilled(1)
sweetPotato.addCondiments("孜然")
print(sweetPotato)
sweetPotato.grilled(1)
sweetPotato.addCondiments("辣椒面")
print(sweetPotato)
sweetPotato.grilled(1)
sweetPotato.addCondiments("甜面酱")
print(sweetPotato)
sweetPotato.grilled(1)
sweetPotato.addCondiments("香菜")
print(sweetPotato)
sweetPotato.grilled(1)
sweetPotato.addCondiments("腐乳")
print(sweetPotato)