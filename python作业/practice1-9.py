# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:56:55 2019

@author: 18364
"""

dic={
     0:
         {
             '电影名':['电影1'],
             '导演':['导演1'],
             '演员':['演员1','演员2','演员3','演员4']
             },
                 
      1:
          {
             '电影名':['电影2'],
             '导演':['导演2'],
             '演员':['演员3','演员2','演员4','演员5']
             },
      2:
          {
             '电影名':['电影3'],
             '导演':['导演3'],
             '演员':['演员1','演员5','演员3','演员6']
             },
      3:
          {
             '电影名':['电影4'],
             '导演':['导演1'],
             '演员':['演员1','演员4','演员3','演员7']
             },
      4:
          {
             '电影名':['电影5'],
             '导演':['导演2'],
             '演员':['演员1','演员2','演员3','演员8']
             },
      5:
          {
             '电影名':['电影6'],
             '导演':['导演3'],
             '演员':['演员5','演员7','演员3','演员9']
             },
      6:
          {
             '电影名':['电影7'],
             '导演':['导演4'],
             '演员':['演员1','演员4','演员6','演员7']
             },
      7:
          {
             '电影名':['电影8'],
             '导演':['导演1'],
             '演员':['演员1','演员4','演员3','演员8']
             },
     8:
          {
             '电影名':['电影9'],
             '导演':['导演2'],
             '演员':['演员5','演员4','演员3','演员9']
             },
     9:
          {
             '电影名':['电影10'],
             '导演':['导演3'],
             '演员':['演员1','演员4','演员5','演员10']
             },
     10:
          {
             '电影名':['电影11'],
             '导演':['导演1'],
             '演员':['演员1','演员4','演员3','演员11']
             },
     11:
          {
             '电影名':['电影12'],
             '导演':['导演2'],
             '演员':['演员7','演员4','演员9','演员12']
             },
     12:
          {
             '电影名':['电影13'],
             '导演':['导演3'],
             '演员':['演员1','演员7','演员9','演员13']
             },
     13:
          {
             '电影名':['电影14'],
             '导演':['导演4'],
             '演员':['演员10','演员4','演员9','演员14']
             },
     14:
          {
             '电影名':['电影15'],
             '导演':['导演5'],
             '演员':['演员1','演员8','演员11','演员15']
             },
     15:
          {
             '电影名':['电影16'],
             '导演':['导演6'],
             '演员':['演员14','演员4','演员13','演员19']
             },
     }
          


d={}
def max_daoyan():
    
    for i in range(16):
        x=dic[i]['导演'][0]
        if not x in d:
            d[x]=1
        else:
            d[x]=d[x]+1 
    v1 = zip(d.values(),d.keys())
    print(v1)
    max_daoyan=max(v1)
    return max_daoyan
m={}
def max_yanyuan():
    
    for i in range(16):
        for x in dic[i]['演员']:
            if not x in m:
                m[x]=1
            else:
                m[x]=m[x]+1
    """
    print(m)
    key_list = []
    value_list = []

    for key, value in m.items():
        key_list.append(key)
        value_list.append(value)
    v2=max(m.values())
    get_value_index = value_list.index(v2)
    print("你要查询的值对应的键为：%s" % key_list[get_value_index])
    """
    v1 = zip(m.values(),m.keys())  
    max_yanyuan=max(v1)
    return max_yanyuan

def max_two_yanyuan():
    c={}
    for i in m.keys():
        for j in range(16):
            if i in dic[j]['演员']:
                for a in dic[j]['演员']:
                    if not i in c:
                        c[i]={}
                    if not a in c[i]:
                        c[i][a]=1
                    else:
                        c[i][a]=c[i][a]+1
        del c[i][i]   
    x=0
    print(c)
    for n in c.keys():
        for e in c[n]:
            if c[n][e]>x:
                x=c[n][e]
                yanyuan1=n
                yanyuan2=e                 
    return yanyuan1,yanyuan2,x


if __name__ == '__main__':    
    print('拍戏最多的导演',max_daoyan())
    print('演戏最多的演员',max_yanyuan())
    print('一起演戏最多的演员',max_two_yanyuan())