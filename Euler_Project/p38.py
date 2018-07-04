# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:02:31 2017

@author: cq_xuke
"""

import time
s=time.clock()
from itertools import count
for n in range(9876,0,-1):
    nstr=str(n)
    for i in count(2):
        nstr+=str(n*i)
        if len(nstr)>=9:
            break
    if sorted(nstr)==list('123456789'):
        print(nstr)
        break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))