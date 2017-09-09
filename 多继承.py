#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class Animal(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        msg=" 名字：%s\n 颜色：%s\n 吃什么：%s\n 叫声：%s\n 跑速：%s\n" % (self.name,self.color,self.eat(),self.bark(),self.run())
        return msg
        

    def eat(self):
        return "吃草。。。。"

    def bark(self):
        return "啊啊啊啊啊啊啊啊啊啊啊啊"

    def run(self):
        return "跑得快....."

class Horse(Animal):
    def bark(self):
        return "嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶嘶"

class Donkey(Animal):
    def bark(self):
        return "咴咴咴咴咴咴咴咴咴咴咴咴"

    def run(self):
        return "跑得一般快....."

class HanXueBaoMa(Horse):
    def run(self):
        return "跑得飞快......."

class Mule(Horse,Donkey):
    def bark(self):
        return "嘘嘘嘘嘘嘘嘘嘘嘘嘘嘘嘘嘘"

    def run(self):
        return "跑得很慢"
def pI(info):
    print(info)

m=Mule("驴","黑灰色")
h=HanXueBaoMa("汗血宝马","红色")
d=Donkey("小叫驴","灰色")
H=Horse("大马","白色")
a=Animal("动物","这个不好说")
pI(m)
pI(h)
pI(d)
pI(H)
pI(a)