#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class Potato:
    def __init__(self):
        self.cooklevel = 0
        self.cookstring = "生的"
        self.condiments = []
    def __str__(self):
        msg = "你的土豆处于 " + self.cookstring + " 状态"
        if len(self.condiments)>0:
            msg += ",添加的佐料："
            for i in self.condiments:
                msg = msg + i + ","
            msg = msg.strip(",")
        return msg
    def cook(self,time):
        self.cooklevel += time
        if self.cooklevel >8:
            self.cookstring = "烤糊的"
        elif self.cooklevel > 5:
            self.cookstring = "烤熟的"
        elif self.cooklevel > 3:
            self.cookstring = "夹生的"
        else:
            self.cookstring = "刚开始烤的"
    def addcondments(self,tmp):
        self.condiments.append(tmp)

sweetPotato = Potato()
print("------开始烤红薯------")
print("------烤两分钟后------")
sweetPotato.cook(2)
print(sweetPotato)
print("------再两分钟后------")
sweetPotato.cook(2)
print(sweetPotato)
print("------添加点芥末------")
sweetPotato.addcondments("芥末")
print("------再加点辣椒------")
sweetPotato.addcondments("辣椒")
print(sweetPotato)
print("------再两分钟后------")
sweetPotato.cook(2)
print(sweetPotato)
print("****好大一个****")
print("****奇葩红薯****")