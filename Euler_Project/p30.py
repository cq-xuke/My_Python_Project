# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:55:48 2017

@author: cq_xuke
"""

import time
s=time.time()
from MyModules.MyFunction import num2digit
count=0
for x in range(2,9**5*6):
    if sum(map(lambda n:n**5,num2digit(x)))==x:
        count+=x
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,2)))