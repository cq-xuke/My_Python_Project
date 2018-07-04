# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:04:01 2017

@author: Tsui
"""
from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
b=1;n=1
while n<=19:
    n+=1
    b=lcm(b,n)
print(b)