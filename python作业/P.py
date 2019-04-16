# -*- coding: utf-8 -*-
"""
软工4班 
张宝
201610414427
谁是小偷
a:我不是
b:c是
c:d是
d:c说的是假的
"""
x=["a","b","c","d"]
for thief in x:
    sum=(thief!='a')+(thief=='c')+(thief=='d')+(thief!='d')
    if sum==3:
        print("小偷是:",thief)
        break
    

