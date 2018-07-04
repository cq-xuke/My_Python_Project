# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:22:55 2017

@author: cq_xuke
"""

import time
s=time.clock()
rev=lambda n:int(str(n)[-1::-1])
count=0
for n in range(1,10001):
    now=n
    for i in range(50):
        now+=rev(now)
        if str(now)==str(now)[-1::-1]:
            break
    else:
        count+=1
print(count)
print("Runing time: %0.3f" %(round(time.clock()-s,3)))