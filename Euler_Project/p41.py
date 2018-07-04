# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:36:43 2017

@author: cq_xuke
"""

import time
s=time.clock()
from itertools import permutations
from functools import reduce
from MyModules.MyFunction import isprime
pool='987654321'
flag=True
for i in range(len(pool)):
    if flag==False:
        break
    for each in permutations(pool[i:]):
        n=int(reduce(lambda x,y:x+y,each))
        if isprime(n):
            print(n);flag=False
            break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))