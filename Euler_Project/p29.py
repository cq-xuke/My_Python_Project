# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:48:32 2017

@author: cq_xuke
"""

import time
s=time.time()
time.time()
terms=set(a**b for a in range(2,101) for b in range(2,101))
print(len(terms))
print('Runing time: {0}s'.format(round(time.time()-s,3)))