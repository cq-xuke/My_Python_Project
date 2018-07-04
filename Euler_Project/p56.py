# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:40:44 2017

@author: cq_xuke
"""

import time
s=time.clock()
best=0
for a in range(1,100):
    for b in range(1,100):
        num=sum(map(int,str(a**b)))
        if num>best:
            best=num
print(best)
print("Runing time: %0.3f" %(round(time.clock()-s,3)))