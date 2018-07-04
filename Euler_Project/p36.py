# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:33:33 2017

@author: cq_xuke
"""

import time
s=time.clock()
count=0
for n in range(1000000):
    decimal=str(n)
    binary=bin(n)[2:]
    if decimal==decimal[-1::-1] and binary==binary[-1::-1]:
        count+=n
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))