# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 21:21:13 2017

@author: cq_xuke
"""

import time
from MyModules.MyFunction import divisor
s=time.time()
isabundant=lambda n:sum(divisor(n)[0:-1])>n
abunnum_list=list(filter(isabundant,range(1,28123)))
twoab=set()
for i in range(len(abunnum_list)):
    for j in range(i,len(abunnum_list)):
        N=abunnum_list[i]+abunnum_list[j]
        if N<28123:
            twoab.add(N)
        else:
            break
num=set(range(1,28123))
nottwoab=num-twoab
print(sum(nottwoab))
print('Runing time: {0}s'.format(round(time.time()-s,3)))