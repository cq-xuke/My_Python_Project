# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:06:19 2017

@author: cq_xuke
"""

import time
s=time.time()
from math import factorial
count=0
for n in range(10,factorial(9)*8):
    if sum(map(factorial,map(lambda n:ord(n)-48,str(n))))==n:
        count+=n
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,3)))