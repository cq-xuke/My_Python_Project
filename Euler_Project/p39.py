# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:22:37 2017

@author: cq_xuke
"""

import time
s=time.clock()
best=0
for p in range(12,1001):
    count=0
    for a in range(3,p//3+1): #a+b+c=p,a<=b<c---->3a<p----> a<p/3
        for b in range(max(a,p//2-a),p//2+1): #a+b+c=p and a+b>c---->a+b>p/2 and b>=a
            c=p-a-b
            if c<b:
                break
            elif a**2+b**2==c**2:
                count+=1
    if count>best:
        best,pbest=count,p
print(pbest)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))