# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:09:32 2017

@author: Tsui
"""

import time
s=time.clock()
def divisor(n):
    d_list=[]
    for i in range(1,int(n**0.5)+1):
        if n % i ==0:
            d_list.extend([i,n//i])
    return set(sorted(d_list))
k=1;divisors={1}
while len(divisors)<=500:
    k+=1
    n=sum(range(1,k))
    divisors=divisor(n)
print(n)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))