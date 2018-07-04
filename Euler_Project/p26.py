# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:14:23 2017

@author: cq_xuke
"""

import time
s=time.time()
def wipe2or5(n):
    while n%2==0:
        n=n//2
    while n%5==0:
        n=n//5
    return n

longest=0
for n in range(1,1000):
    if wipe2or5(n)==1:
        continue
    N=wipe2or5(n)
    start='9'
    while int(start) % N != 0:
        start+='9'
    period=len(start)
    if period>longest:
        longest=period
        best_n=n
print(best_n)
print('Runing time: {0}s'.format(round(time.time()-s,3)))