# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:32:07 2017

@author: cq_xuke
"""

import time
s=time.clock()
import itertools as it
dstr=''
for n in it.count(1):
    if len(dstr)<=1000000:
        dstr+=str(n)
    else:
        break
print(int(dstr[0])*int(dstr[9])*int(dstr[99])*int(dstr[999])\
      *int(dstr[9999])*int(dstr[99999])*int(dstr[999999]))
print('Runing time: {0}s'.format(round(time.clock()-s,3)))