# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:39:57 2017

@author: cq_xuke
"""

import time
s=time.clock()
from MyModules.MyFunction import primeiter,isprime
for p in primeiter(1488):
    for i in range(1,3):
        plus=p+i*3330
        if not isprime(plus):
            break
        else:
            plus_list=sorted(map(int,str(plus)))
            p_list=sorted(map(int,str(p)))
            if p_list != plus_list:
                break
    else:
        print(p,p+3330,p+3330*2,sep='')
        break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))