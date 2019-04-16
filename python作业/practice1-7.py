# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:14:12 2019

@author:
软工4班 
张宝
201610414427
问题:一个小偷打劫一个保险箱，保险箱中有5中物品，
每种物品的重量不同价值也不同，物品的重量与价值
如表5.2所示，小偷的背包只能负重8公斤，要怎样才
能使偷走的物品总价值最大？（动态规划思想）
"""
w=[0,4,5,2,1,6] #物品重量
v=[0,45,57,22,11,67] #物品价值
n=len(w)-1 #物品数量
m=8 #背包承重

x=[] #放入物品顺序
value=0 #背包价值
a=[[0 for col in range(m + 1)] for raw in range(n + 1)]
 #表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值

def chief(w,v,n,m,value):
    for i in range(1, n + 1):      
        for j in range(1, m + 1):   
            if (j >= w[i]):
                a[i][j] = max(a[i - 1][j], a[i - 1][j - w[i]] + v[i])   
            else:
                a[i][j] = a[i - 1][j]

    j = m
    for i in range(n, 0, -1):
        if a[i][j] > a[i - 1][j]:
            x.append(i)
            j = j - w[i] 
    value=a[n][m]
    return value
print( "最大值为：" + str(chief(w,v,n,m,value)))
print ("物品的顺序：",x)

