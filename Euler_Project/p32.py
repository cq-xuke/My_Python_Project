# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 20:18:11 2017

@author: cq_xuke
"""

import time
import itertools as it
from MyModules.MyFunction import digit2num,num2digit
s=time.time()
count=0
for dresult in it.permutations([1,2,3,4,5,6,7,8,9],4):
    result=digit2num(dresult)
    for n in range(1,int(result**0.5+1)):
        if result % n ==0:
            total=num2digit(n)+num2digit(result//n)+list(dresult)
            if sorted(total)==[1,2,3,4,5,6,7,8,9]:
                count+=result
                break
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,3)))
