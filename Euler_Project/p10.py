# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:34:41 2017

@author: Tsui
"""
import time
s=time.clock()
from MyModules.MyFunction import primes
primes_list=primes(2000000)
print(sum(primes_list))
print('Runing time:',round(time.clock()-s,2))