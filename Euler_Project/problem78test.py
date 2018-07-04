# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:01:16 2017

@author: cq_xuke
"""
import time
start=time.clock()
pentagonal=[0]
for N in range(1,50000):
    pentagonal.append(N*(3*N-1)//2)
    M=-N
    pentagonal.append(M*(3*M-1)//2)

pdic={0:1}
from numba import jit,int64
@jit(int64())
def minn():
    for n in range(1,100000):
        knext=n;i=1;s=0
        while knext>=0:
            k=n-pentagonal[i]
            sign=(-1)**int((i+1)/2+1)
            s+=sign*pdic[k]
            i=i+1
            knext=n-pentagonal[i]
        pdic[n]=s
        if s%1000000==0:
            print(n)
            break
minn()
end=time.clock()
print(end-start)