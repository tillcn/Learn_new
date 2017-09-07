#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
class A(object):
    def test(self):
        self.name = "我是A"
        print(self.name)

class B(object):
    def test(self):
        self.name = "我是B"
        print(self.name)

class C(A):
    pass

class D(A,B):
    pass

class E(B,A):
    pass

print("----- a ------")
a=A()
a.test()

print("----- b ------")
b=B()
b.test()

print("----- c ------")
c=C()
c.test()

print("----- d ------")
d=D()
d.test()

print("----- e ------")
e=E()
e.test()
