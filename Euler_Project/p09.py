# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 00:16:00 2017

@author: Tsui
"""

flag=True
for i in range(1,1001):
    if flag==False:
        break
    for j in range(1,i+1):
        k=1000-i-j
        if k<=0:
            break
        ijklist=sorted([i,j,k])
        if ijklist[2]**2==ijklist[1]**2+ijklist[0]**2:
            print(i*j*k)
            flag=False
            break