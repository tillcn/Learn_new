#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class Home:
    '''此为操作类、调用类的实例
重点是 Furniture 类的get方法
跟 Home 类中的调用 Furniture类中属性的方法'''
    def __init__(self,area):
        self.area = area
        self.rongNaList = []
        self.light = 'off'

    def __str__(self):
        msg = "家当前可用面积："+ str(self.area)+";灯的状态为："+self.light
        if len(self.rongNaList) > 0:
            msg += "，当前已容纳的物品有："
            for i in self.rongNaList:
                msg = msg+i.getBedName()+","
            msg = msg.strip(",")
        return msg

    def rongNa(self, item):
        bedArea = item.area#item.getBedArea()
        if self.area > bedArea:
            self.rongNaList.append(item)
            self.area -= bedArea
            print("放置%s成功..放置后还剩余面积为%d"% (item.name,self.area))
        else:
            print("当前需放置家具面积大于房子可用的面积")

    def lightOn(self):
        self.light = 'on'
        for temp in self.rongNaList:
            temp.setlight()




class Furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.light = "off"

    def __str__(self):
        msg = self.name + "占用的面积为：" + str(self.area)+";当前明暗程度为："+self.light
        return msg

    def getBedArea(self):
        return self.area

    def getBedName(self):
        return self.name

    def setlight(self):
        self.light = "on"

    def setlightoff(self):
        self.light = 'off'

home=Home(131)
#print(home,"\n")

bed = Furniture("硬板床",4)
print(bed)
home.rongNa(bed)
#print(home,"\n")

bed2 = Furniture("席梦思",3)
print(bed2)
home.rongNa(bed2)
#print(home,"\n")

washingMachine = Furniture("洗衣机",2)
print(washingMachine)
home.rongNa(washingMachine)
#print(home,"\n")

Helicopter = Furniture("直升机",200)
print(Helicopter)
home.rongNa(Helicopter)
#print(home,"\n")

home.lightOn()
print(home)

#想一想这里的内容是怎么产生的。
for i in home.rongNaList:
    print(i)
