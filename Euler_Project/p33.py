# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:49:34 2017

@author: cq_xuke
"""

import time
s=time.time()
from fractions import Fraction
def isstrange(num,den):
    flag=False
    numdigit=set(map(lambda n:ord(n)-48,str(num)))
    dendigit=set(map(lambda n:ord(n)-48,str(den)))
    if len(numdigit)==len(dendigit)==1: #e.g.(11,22) must be removed
        pass
    elif numdigit&dendigit=={0}: #e.g. (30,50) must be sifted
        pass
    else:
        cnd=numdigit-(numdigit&dendigit)
        cdd=dendigit-(numdigit&dendigit)
        if len(cnd)!=1 or len(cdd)!=1: #cnd and cdd could just have one element
            return flag
        try:
            if Fraction(list(cnd)[0],list(cdd)[0])==Fraction(num,den):
                flag=True
        except ZeroDivisionError: #e.g.(12,20) will result in Fraction(1,0)
            pass
            
    return flag
        
frac=Fraction(1,1)
for num in range(10,99):
    for den in range(num+1,100):
        if isstrange(num,den):
            frac*=Fraction(num,den)
print(frac.denominator)
print('Runing time: {0}s'.format(round(time.time()-s,3)))