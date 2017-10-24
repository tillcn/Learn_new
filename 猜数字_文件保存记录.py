#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
name = input('请输入你的名字:')
with open('Score.txt','r') as f:
    lines = f.readlines()
scores = {}                                         #初始化一个空字典
for l in lines:
    s = l.split()                                   #把每一行的数据拆分成list
    scores[s[0]] = s[1:]                            #把第一项作为key,剩下的作为value
score = scores.get(name)                            #查找当前玩家的数据
if score is None:                                   #如果没找到
    score = [0,0,0]                                 #初始化数据
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0
print('%s,你已经玩了%d次,最少%d轮猜出答案,平均%.2f猜出答案' % (name,game_times,min_times,avg_times))
com = random.randint(1, 100)
times = 0
guess=True
while guess:
    people = input('请输入你的选择(1-100),退出请输入q，查询成绩请输入c：')
    times += 1
    if people.isdigit() and 0 < int(people) < 101:
        peo = int(people)
        if peo == com:
            print('恭喜你，猜对了。')
            guess = False
        elif peo > com:
            print('你输入的数字太大。')
        elif peo < com:
            print('你输入数字太小')
    elif people == 'q' or people == 'Q':
        break
    elif people == 'c' or people == 'C':
        print('pass')
    else:
        print('你的输入有误，请重新输入')
if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1
scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
    line = n+' ' + ' '.join(scores[n]) + '\n'
    result += line
with open('Score.txt','w') as f:
    f.write(result)


