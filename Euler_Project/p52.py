# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 20:41:00 2017

@author: cq_xuke
"""

import time
s=time.clock()
from itertools import count
flag=False
for wei in count(3):
    if flag==True:
        break
    for n in range(10**wei,int(10**(wei+1)/6)):
        for num in range(1,7):
            if sorted(str(num*n))!=sorted(str(n)):
                break
        else:
            flag=True;print(n)
            break
print("Runing time: %0.3f" %(round(time.clock()-s,3)))