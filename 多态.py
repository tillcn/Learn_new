#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class Animal(object):
    def bark(self):
        print("啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊")

class Dog(Animal):
    def bark(self):
        print("汪汪汪汪汪汪汪汪汪汪汪汪汪汪汪汪汪汪汪")

class Cat(Animal):
    def bark(self):
        print("喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵")

class Goat(object):                  #注意看他的继承对象
    def bark(self):
        print("咩咩咩咩咩咩咩咩咩咩咩咩咩咩咩咩咩咩咩")

def shout(name):
    name.bark()

print("---------我是Animal----------")
a=Animal()
shout(a)

print("\n")
print("----------我是Dog-----------")
d=Dog()
shout(d)

print("\n")
print("----------我是Cat-----------")
c=Cat()
shout(c)

print("\n")
print("----------我是Goat-----------")
g=Goat()
shout(g)

print("\n")
print("这就是多态，还有python崇尚的鸭子类型：声音像鸭子，走路像鸭子，就看做鸭子，\n"
      "比如Goat不属于Animal类型，但里边有bark方法，那shout就能调用")