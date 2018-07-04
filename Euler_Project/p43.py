# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:51:02 2017

@author: cq_xuke
"""

import time
s=time.clock()
from itertools import permutations
from functools import reduce
primes=[2,3,5,7,11,13,17]
count=0
for pandigits in permutations([9,8,7,6,5,4,3,2,1,0]):
    if pandigits[0]==0:
        break
    i=1
    for p in primes:
        pan=reduce(lambda x,y:x*10+y,pandigits[i:i+3])
        i+=1
        if pan % p != 0:
            break
    else:
        count+=reduce(lambda x,y:x*10+y,pandigits)
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))