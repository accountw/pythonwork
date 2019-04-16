# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:37:54 2019

@author: 
软工4班 
张宝
201610414427
求1000以内素数和
"""
from math import sqrt
def sushu(n):
    temp=int(sqrt(n))
    for j in range(2,temp+1):
        if n%j==0:
            return False
    else:
        return True

def main():
    sum=2
    for i in range(3,1000,2):
        if sushu(i):
            sum=sum+i
    print(sum)
main()

