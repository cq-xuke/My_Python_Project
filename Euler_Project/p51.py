# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:55:54 2017

@author: cq_xuke
"""
import time
s=time.clock()
from MyModules.MyFunction import primeiter,isprime
flag=False
for p in primeiter(56993):
    if flag==True:
        break
    pstr=str(p)
    for rep in ['0','1','2']:
        if pstr.count(rep)>=2:
            k=0
            for i in range(int(rep),10):
                if isprime(int(pstr.replace(rep,str(i)))):
                    k+=1
            if k==8:
                print(p)
                flag=True
                break
print("Runing time: %0.3f" %(round(time.clock()-s,3)))