#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name = "my \tname is {name} and i am {year} old"

print(name.capitalize())                                #首字母大写
print(name.count("a"))                                  #统计出现次数
print(name.center(50,"-"))                              #一共打多少，字符不足以哪个代替
print(name.endswith("ex"))                              #判断以哪个结尾  结果为True或False
print(name.expandtabs(tabsize=30))                      #tab转成多少个空格
print(name[name.find("name"):])                         #查找字符下标
print(name.format(name='Lee',year=35))                  #格式化
print(name.format_map(  {'name':'Lee','year':35}  ))    #另一种格式化，能看懂就行，用得极少
print('ab23'.isalnum())                                 #判断是否为阿拉伯数字(包含英文字符和数字,小数)
print('abA'.isalpha())                                  #纯英文字符
print('1A'.isdecimal())                                 #是不是十六进制
print('1A'.isdigit())                                   #是不是一个整数
print('a 1A'.isidentifier())                            #是不是一个合法的标识符(通俗一点说，是不是一个合法的变量名)
print('33A'.isnumeric())                                #是不是只包含合法的数字，小数点也不行
print('My Name Is  '.istitle())                         #每个单词开关是否大写
print('My Name Is  '.isprintable())                     #是否可被打印，linux设备文件等是不能被打印的
print('My Name Is  '.isupper())                         #是否大写
print('+'.join( ['1','2','3'])  )                       #列表转字符串,列表中是int类型的不行
print( name.ljust(50,'*')  )                            #两个参数，长度，补全符号，保证长50，不够用*补上
print( name.rjust(50,'-')  )                            #与上一样，在前面补全
print( 'Lee'.lower()  )                                 #把大写变小写
print( 'Lee'.upper()  )                                 #把小写变大写
print( '\nLee'.lstrip()  )                              #掉右边的某个字符或符号，默认是空格或回车
print( 'Lee\n'.rstrip()  )                              #掉左边的某个字符或符号，默认是空格或回车
print( '    Weeds\n'.strip()  )                         #两边同时去掉
p = str.maketrans("abcdefli",'123$@456')                #把前面的字符串转成后面的字符串的值，看下面的例子，前后数量要对应
print("Weeds li".translate(p) )

print('Weeds li'.replace('l','L',1))                    #替换，把l替换成L，后面表示换几个，从左往右
print('Weeds lil'.rfind('l'))                           #从右往左查找，返回的值是从左往右的下标，只是找到的是最右的边的l
print('1+2+3+4'.split('+'))                             #把字符串按空格分成列表，被当时分割符的字符会被去掉
print('1+2\n+3+4'.splitlines())                         #按换行符来分割字符转成列表
print('Weeds Li'.swapcase())                            #大小写转换
print('Weeds li'.title())                               #变成一个title 每次字符开头换成大写
print('Weeds li'.zfill(50))                             #自动补0，十六进制有用