#!/usr/bin/env python3
#--*--coding:utf-8--*--
class shortInputException(Exception):
    """自已定义的异常类"""
    def __init__(self, length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        

try:
    s = input("请输入点什么:")
    if len(s) < 3:
        raise shortInputException(len(s),3)
except EOFError:
    print("你输入一个结束标记EOF")
except shortInputException as x:
    print('shortInputException:输入的长度是 %d,长度至少应该是%d'% (x.length,x.atleast))
else:
    print('没有异常产生')
finally:
    print('不管有没有异常都会执行')