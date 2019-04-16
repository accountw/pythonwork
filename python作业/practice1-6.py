# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:32:05 2019

@author:
软工4班 
张宝
201610414427
假设玩具小汽车x元一辆，小明用y元买z辆，如何找零使得找零纸张数最少
"""

number=[0,0,0,0,0]
values=[50,20,10,5,1]
value=12
def pay(charge):
    for i in range(5):
        if charge>values[i] or charge==values[i]:
            number[i]=charge//values[i]
            charge=charge-number[i]*values[i]
    return number
    
    
    
    
    
def main():
    while(1):
        num=int(input("车辆单价%d元,请输入你要买的辆数:" %(value)))
        if num<0:
            print("输入错误，请重新输入")
            continue
        elif num==0:
            print("你没有购买车辆")
            continue
        else:
            break
    while True:
        charge=int(input("请投入你的钱:"))
        if charge-num*value<0:
            print("投钱过少，请重新投入")
            continue
        elif charge-num*value==0:
            print("不用找零")
            break
        else:
            numbers=pay(charge-num*value)
            break
    for i in range(5):
            print("找零%d元:%d张" %(values[i],numbers[i]))
            
main()
    
        
    
        