# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:22:04 2017

@author: cq_xuke
"""

import time
s=time.clock()
num=sum(map(lambda x:x**x,range(1,1001)))
print(num % 10**10)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))