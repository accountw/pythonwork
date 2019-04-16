5# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:41:18 2019

@author: 
软工4班 
张宝
201610414427
猴子50阶，一次跳1，2，3阶，多少跳法
递归函数
"""
i=0
def jump(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return jump(n-3)+jump(n-2)+jump(n-1)
    
    
def main():
    x=int(input("请输入梯子阶数:"))
    print(jump(x))
main()
