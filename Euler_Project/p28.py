# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:15:47 2017

@author: cq_xuke
"""

import time
import itertools as it
s=time.time()
size=1001
dig2=it.chain((n**2 for n in range(3,size+1,2)),(N**2+1 for N in range(2,size,2)))
dig1=it.chain((m**2-m+1 for m in range(3,size+1,2)),(M**2+1-M for M in range(2,size,2)))
print(sum(dig1)+sum(dig2)+1)
print('Runing time: {0}s'.format(round(time.time()-s,3)))