# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 23:12:40 2017

@author: Tsui
"""

import time
s=time.clock()
from MyModules.MyFunction import isprime
count=1;n=3
while count<=10000:
    if isprime(n):
        count+=1
    n+=2
print(n-2)
print('time=',time.clock()-s)