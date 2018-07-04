# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:15:37 2017

@author: cq_xuke
"""

import time
s=time.clock()
from MyModules.MyFunction import nchoosek
count=0
for n in range(1,101):
    for k in range(1,n+1):
        if nchoosek(n,k)>1000000:
            count+=1
print(count)
print("Runing time: %0.3f" %(round(time.clock()-s,3)))