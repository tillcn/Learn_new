#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d={'name':'lee','age':18,'gender':'boy','del':[1,2,3]}      #字典是键值对，健为不可变对象，value可以是list,tuple等对象
#增
d['score'] = 100
#删
del d['del']                                                #删除key为'del'的键值对，如果不存在将服错
#改
d['score'] = 120
#查
d['name']
#方法
len(d)                                                      #一对健值对做为一个元素返回
str(d)                                                      #以可打印的字符串表示
d1=d.copy()                                                 #返回一个字典的浅复制
d1.clear()                                                  #清空字典内所有元素
seq=('name','age')
d.fromkeys(seq, 10)                                         #用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值,如果没初始值，默认为None
d.get('name')                                               #返回指定键的值，如果值不在字典中返回None
d.keys()                                                    #返回所有的key
d.items()                                                   #以列表方式返回可遍历的(键, 值) 元组数组
d.pop(key, default)                                         #删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值
d.popitem()                                                 #随机返回并删除字典中的一对键和值(一般删除末尾对),如果字典已为空，调用此方法，报KeyError异常
d.setdefault(key, default=None)                             #和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
d2={'wow':'love'}
d.update(d2)                                                #把d2的键/值对更新到d里
d.values()                                                  #以列表返回字典中的所有值