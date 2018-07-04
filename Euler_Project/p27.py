# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:33:16 2017

@author: cq_xuke
"""

import time
from MyModules.MyFunction import isprime
s=time.time()
def Quadratic_primes(a,b):
    n=0
    if not isprime(n**2+a*n+b):
        return
    else:
        while isprime(n**2+a*n+b):
            n+=1
    return n-1

def primeiter(init):
    if init<=2:
        init=2
    while not isprime(init):
        init+=1
    yield init
    if init==2:
        init=3
        while True:
            if isprime(init):
                yield init
            init+=2
    else:
        init+=2
        while True:
            if isprime(init):
                yield init
            init+=2

it=primeiter(2)
best=0
b=next(it)
while b<1000:
    for a in range(2-b,1000):
        num=Quadratic_primes(a,b)
        if num is None:
            continue
        if num>best:
            best,best_ab=num,a*b
    b=next(it)
print(best_ab)
print('Runing time: {0}s'.format(round(time.time()-s,3)))