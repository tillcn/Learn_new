#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class result:
    '''
    一、面向过程
    1、提示用户输入数据    print()
    2、接收数据           w=input()
    3、计算              result = a+b
    4、输出              print(result)

    保存数据 ======> 变量 (str,int，列表，元组，字典)
    保存一块代码======> 函数
    把数据和代码保存起来当做一个整体======> 对象

    二、面向对象
    1、先定义一个类
    2、类是一个模板
    3、创建一个对象
    4、对象.方法/属性
    '''
#放在外面叫函数
def fun1():
    pass

#函数调用
fun1()

#放在类里边叫方法/属性
class class1:
    def fun2(self):
        pass

    def __init__(self,name):    #设置默认属性
        self.__name = name

    def __str__(self):         #设置默认输出
        print(self.__name)

    def __del__(self):
        pass


#创建对象 (方法/属性调用)
l = class1()
l.fun2()