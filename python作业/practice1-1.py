# -*- coding: utf-8 -*-
"""
软工4班 
张宝
201610414427
"""
x=int(input("请输入pm2.5:"))
if x<35:
    print("优")
elif x<75:
    print("良")
elif x<115:
    print("轻度污染")
elif x<150:
    print("中度污染")
elif x<250:
    print("重度污染")
elif x<500:
    print("严重污染")
else:
    print("输入错误")
    
