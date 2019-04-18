# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:12:24 2019

@author: 张宝
"""
#-*- coding: utf-8 - 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
import numpy as np

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=12)

result = pd.read_csv('D:\pythonwork\pollution.csv')
def avgpm():
    grouped = result['pm2.5'].groupby(result['year'])
    plt.bar([2010,2011,2012,2013,2014],[grouped.mean().loc[2010],grouped.mean().loc[2011],
        grouped.mean().loc[2012],grouped.mean().loc[2013],grouped.mean().loc[2014]])
    plt.xlabel('year')
    plt.ylabel('pm2.5')
    plt.title(u'平均PM2.5',fontproperties=font)
    plt.show()

def avgTemp():
    grouped = result['TEMP'].groupby(result['year'])
    plt.bar([2010, 2011, 2012, 2013, 2014], [grouped.mean().loc[2010], grouped.mean().loc[2011],
                                             grouped.mean().loc[2012], grouped.mean().loc[2013],
                                             grouped.mean().loc[2014]])
    plt.xlabel('year')
    plt.ylabel('TEMP')
    plt.title(u'平均气温', fontproperties=font)
    plt.show()

def shiyan2():
    d=[] #日期
    d1=[]
    y=[] #PM2.5
    i=0
    t=[] #气温
    PRES=[] #气压
    Iws=[] #降雨量
    for index, row in result.iterrows():
        if row['pm2.5']!=None:
           d.append((str(row['year'])+'年'+str(row['month'])+'月'+str(row['day'])+'日'+str(row['hour'])+'时'))
           y.append(row['pm2.5'])
        d1.append((str(row['year']) + '年' + str(row['month']) + '月' + str(row['day']) + '日'+str(row['hour'])+'时'))
        t.append(row['TEMP'])
        PRES.append(row['PRES'])
        Iws.append(row['Iws'])
    plt.subplot(221)
    plt.plot(d, y)
    plt.xlabel(u'日期2010-2014', fontproperties=font)
    plt.ylabel('pm2.5')
    plt.title(u'pm2.5趋势', fontproperties=font)
    plt.xticks([])
    plt.subplot(222)
    plt.plot(d1, t)
    plt.xlabel(u'日期2010-2014', fontproperties=font)
    plt.ylabel(u'气温', fontproperties=font)
    plt.title(u'气温趋势', fontproperties=font)
    plt.xticks([])
    plt.subplot(223)
    plt.plot(d1, PRES)
    plt.xlabel(u'日期2010-2014', fontproperties=font)
    plt.ylabel(u'气压', fontproperties=font)
    plt.title(u'气压趋势', fontproperties=font)
    plt.xticks([])
    plt.subplot(224)
    plt.plot(d1, Iws)
    plt.xlabel(u'日期2010-2014', fontproperties=font)
    plt.ylabel(u'降雨量', fontproperties=font)
    plt.title(u'降雨量趋势', fontproperties=font)
    plt.xticks([])
    plt.show()

def shiyan3():
    i=[]
    b=[['' for col in range(5)] for raw in range(31)]
    a=[['' for col in range(5)] for raw in range(31)]
    pm= result['pm2.5'].groupby([result['year'], result['month'],result['day']]).mean()
    grouped = result['pm2.5'].groupby([result['year'],result['month']]).mean().sort_values(ascending=False)
    for x in range(0,5):
        i.append(grouped.index[x])
    for x in range(5):
        b[x]=pm[i[x]]
    print(i[0][0])
    Color=['blue','green','red','yellow','pink']
    for x in range(5):
        label=(str(i[x][0])+'.'+str(i[x][1]))
        plt.plot(b[x].index, b[x],color=Color[x], label=label)
    plt.legend(loc='upper left')
    plt.xlabel(u'日期', fontproperties=font)
    plt.ylabel('pm2.5')
    plt.title(u'pm2.5趋势', fontproperties=font)
    plt.show()
    '''
    for x in range(0, 5):
        j=0
        for row in result.iterrows():
            
            if row['year'] ==i[x][0]:
                if row['month'] ==i[x][1]:
                    print(row['day'])
                    q[x][j]=str(row['year']) + '年' + str(row['month']) + '月' + str(row['day']) + '日'+str(row['hour'])+'时'
                    j=j+1
    '''
if __name__ == '__main__':
     # avgpm() #第一个 ,平均pm
    avgTemp() #第一个,平均气温
    shiyan2() #第二个
    shiyan3()
