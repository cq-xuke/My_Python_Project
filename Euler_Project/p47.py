# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:38:34 2017

@author: cq_xuke
"""

import time
s=time.clock()
from MyModules.MyFunction import factor
from itertools import count
for n in count(646):
    for con in range(n,n+4):
        if len(set(factor(con)))!=4:
            break
    else:
        print(n);break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))