# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:01:24 2017

@author: cq_xuke
"""

import time
s=time.clock()
from MyModules.MyFunction import isprime,primeiter
from itertools import takewhile,count
def oddcomposite():
    for n in count(3,2):
        if not isprime(n):
            yield n

for n in oddcomposite():
    for p in takewhile(lambda x:x<n,primeiter()):
        if int(((n-p)/2)**0.5)==((n-p)/2)**0.5:
            break
    else:
        print(n);break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))