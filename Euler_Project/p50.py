# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:00:53 2017

@author: cq_xuke
"""

import time
s=time.clock()
from MyModules.MyFunction import primeiter,isprime
for i in primeiter():
    count=0
    for p in primeiter(i):
        if count+p>=1000000:
            break
        count+=p
    if isprime(count):
        break
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))