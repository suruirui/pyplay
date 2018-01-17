# -*- coding:utf-8 -*-
#在房屋中存放家具

class House:
    def __init__(self,area,info,addr):
        self.area = area   #总面积
        self.info = info   #户型
        self.addr = addr   #地址
        self.leftArea = area  #可用面积(初始为总面积)
        self.containItems = []  #容纳的家具

    def __str__(self):
        msg = "房子的总面积是:%d,可用面积是:%d,户型是:%s,地址是:%s" % (self.area, self.leftArea,
                                                     self.info, self.addr)
        msg += " 当前房子里的物品有%s" % (str(self.containItems))
        return msg

    #置办家具
    def addItem(self,item):
        if self.leftArea < item.getArea():
            print("没地儿放了～")
            return
        self.leftArea -= item.getArea()  #可用面积减少
        self.containItems.append(item.getName())


class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占用的面积是:%d" % (self.name, self.area)

    def getArea(self):
        return self.area

    def getName(self):
        return self.name

#珠江帝景A坐3号楼C单元402
zjdjA3c402 = House(129,'三室一厅','北京市朝阳区大望路666号')
print(zjdjA3c402)

bed1 = Bed("席梦思",4)
print(bed1)
zjdjA3c402.addItem(bed1)
print(zjdjA3c402)

superBed = Bed("超大蹦床",150)
print(superBed)
zjdjA3c402.addItem(superBed)
print(zjdjA3c402)
