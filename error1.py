#!/usr/bin/env python3
#--*--coding:utf-8--*--
import os
try:
	print("------test-----")
	open('123.py',"r")
	print("------test-----")
except IOError:
	print("你要的文件不存在")

try:
	print("------test1-----")
	print(num)
	print("------test1-----")
except NameError as errmsg:
	print("请修正错误：%s"%errmsg)
finally:
	print('不管有没有错误都会执行')

