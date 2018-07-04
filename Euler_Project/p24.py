# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:59:25 2017

@author: cq_xuke
"""

import time
from MyModules.MyFunction import digit2num
from itertools import permutations
s=time.time()
count=0
for digits in permutations([0,1,2,3,4,5,6,7,8,9]):
    count+=1
    if count==1000000:
        break
print(digit2num(digits))
print('Runing time: {0}s'.format(round(time.time()-s,3)))