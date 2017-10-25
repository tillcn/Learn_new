#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
name = input('请输入你的名字:')
with open('Score.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
scores = {}                                         #初始化一个空字典
for l in lines:
    s = l.split()                                   #把每一行的数据拆分成list
    scores[s[0]] = s[1:]                            #把第一项作为key,剩下的作为value
score = scores.get(name)                            #查找当前玩家的数据
if score is None:                                   #如果没找到
    score = [0,0,0]                                 #初始化数据
game_times = int(score[0])                          #把第一个数值初始为玩了几次(程序运行过几次)
min_times = int(score[1])                           #把第二个数值初始为最少猜出来的轮数
total_times = int(score[2])                         #第三个数值初始为一共猜了多少回
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print('%s,你已经玩了%d次,最少%d轮猜出答案,平均%.2f猜出答案' % (name,game_times,min_times,avg_times))
com = random.randint(1, 100)
times = 0
while True:
    people = input('请输入你的选择(1-100):')
    times += 1
    if people.isdigit() and 0 < int(people) < 101:
        peo = int(people)
        if peo == com:
            print('恭喜你，猜对了。')
            break
        elif peo > com:
            print('你输入的数字太大。')
        elif peo < com:
            print('你输入数字太小')
    else:
        print('你的输入有误，请重新输入')
if game_times == 0 or times < min_times:
    min_times = times
total_times += times                                                            #猜的总次数
game_times += 1                                                                 #玩了多少回
scores[name] = [str(game_times),str(min_times),str(total_times)]                #把上面的数值以name为key名存为value
result = ''                                                                     #定义一个空字段
for n in scores:                                                                #for循环字典n得到的是每一项的key, scores[n]就是对应的value
    line = n+' ' + ' '.join(scores[n]) + '\n'                                   #n就key，scores是值     .join 列表转字符串                              
    result += line
with open('Score.txt','w',encoding='utf-8') as f:
    f.write(result)