# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:40:56 2017

@author: cq_xuke
"""

import time
s=time.clock()
import MyModules.MyFunction as MF
def istrunc(n):
    flag=False
    if n>10:
        strn=str(n)
        s1=s2=strn
        for k in range(len(strn)-1):
            s1=s1[:-1]
            s2=s2[1:]
            if not (MF.isprime(int(s1)) and MF.isprime(int(s2))):
                break
        else:
            flag=True
    return flag
    
count=i=0
for p in MF.primeiter():
    if istrunc(p):
        i,count=i+1,count+p
    if i==11:
        break
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))