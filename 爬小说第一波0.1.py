#!/usr/bin/env python3
# -*-coding:utf-8-*-
#小说爬虫
#目前针对网站(#www.biqukan.com)
#vision 0.1
#mpage_url : 小说目录主页地址
#cpage_url : 小说各章地址
#chapters : 章节列表
#cname : 章节名称

from bs4 import BeautifulSoup
from urllib import request
import sys
import re
import requests

fileName=input("请输入小说名：")
file = open(fileName+".txt","w",encoding="utf-8")
#选定小说目录主页，确定头文件和客户运行环境
mpage_url=input("请输入小说章节页的地址：")
head = {}
head["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
#抓取小说主页源文件内容，并转码成中文 第一种逻辑方法
#mpage_req = urllib.request.Request(url = mpage_url , headers = head)
#mpage_res = urllib.request.urlopen(mpage_req)
#mpage_html = mpage_res.read().decode("gbk", "ignore")
#第二种逻辑方法更简单直白,输出的文本要带.text才行
mpage_res = requests.get(url = mpage_url , headers = head)
#将爬下的主页源文件用Beautiful拓展
#用chrome的开发工具，查看主页可以发现，章节及链接内容所在
soup = BeautifulSoup(mpage_res.text, "lxml")
#获取章节列表
chapters = soup.select("div.listmain dl a")
list1 = []
list2 = []
ss = 1
for line in chapters:
    chapters_url = "http://www.biqukan.com" + line.get('href')
    chapters_name = line.string
    mpage = chapters_name + ":" + chapters_url
    list1.append(chapters_name)
    list2.append(chapters_url)
chapters_number = []
for ll in list1:
    kkk = ll[:3]
    chapters_number.append(kkk)
if "第一章" in chapters_number:
    i_1 = chapters_number.index("第一章")
if "第1章" in chapters_number:
    i_1 = chapters_number.index("第1章")
if "第00" in chapters_number:
    i_1 = chapters_number.index("第00")
chapters_list = list2[i_1:]
number = len(chapters_list)
for i in chapters_list:
    txt_res = requests.get(url = i, headers = head)
    txt_soup = BeautifulSoup(txt_res.text, "lxml")
    title = txt_soup.select("#wrapper .book .content h1")[0].text.replace("/x0a","")
    txt = txt_soup.select("#wrapper .book .content .showtxt")[0].text.replace("/x0a","")
    file.write(title + "\n\n")
    file.write(txt + "\n\n")
    sys.stdout.write("下载进度:%.1f%%" % float(ss / number*100) + "\r")
    sys.stdout.flush()
    ss+=1
file.close()
