# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:11:42 2017

@author: Tsui
"""

import math
import time
s=time.clock()
flag=False;count=a=0
while flag==False:
    a+=1
    for bc in range(2,2*a+1):
        if math.sqrt(a**2+bc**2)%1==0:
            count+=(bc//2-max(0,bc-a-1))
    if count>1000000:
        print(a)
        flag=True       
print(time.clock()-s)