# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:12:24 2019

@author: 张宝
"""
#-*- coding: utf-8 -
import requests
from bs4 import BeautifulSoup
import csv
import re
import bs4
import pandas as pd
def getHtml(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return(r.text)
    except:
        print("访问目标页面异常!")

def getInfo(html):
    uinfo=[]
    soup=BeautifulSoup(html,'html.parser')
    dic={
        '发帖人':[] ,
        '主题': [],
        '回复数':[] ,
    }
    print(soup.select('.threadlist_rep_num')[0].get_text())

    for x in range(len(soup.select('.threadlist_rep_num'))):
        dd=soup.select('.j_th_tit ')[x].get_text()
        mm = soup.select('.threadlist_rep_num')[x].get_text()
        ss=soup.select('.tb_icon_author ')[x].get_text()
        dic['发帖人'].append(ss)
        dic['主题'].append(dd)
        dic['回复数'].append(mm)
    return  dic


def save(dic):
    pd.DataFrame(dic).to_csv('D:\pythonwork\practice.csv', mode='a', header=False, encoding='utf_8_sig')

if __name__ == '__main__':
    for x in range(10):#爬取抗压吧前10页的帖子
        z=str(x*50)
        print(z)
        url=('https://tieba.baidu.com/f?kw=%E6%8A%97%E5%8E%8B&&ie=utf-8&pn='+z)
        html=getHtml(url)
        MyInfo = getInfo(html)
        save(MyInfo)
    print('完成')




