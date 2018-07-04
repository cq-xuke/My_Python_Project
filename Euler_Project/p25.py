# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:44:19 2017

@author: cq_xuke
"""
import time
s=time.time()
term1=1;term2=1;count=2
while True:
    term=term1+term2
    count+=1
    if len(str(term))==1000:
        print(count)
        break
    term1,term2=term2,term
print('Runing time: {0}s'.format(round(time.time()-s,3)))