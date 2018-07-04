# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:11:46 2017

@author: cq_xuke
"""

import time
s=time.clock()
import itertools as it
import MyModules.MyFunction as MF
def rotation(n):
   r=[n]
   ndigits=MF.num2digit(n)
   if len(ndigits)==1:
       pass
   else:
       for i in range(len(ndigits)-1):
           ndigits[0],ndigits[1:]=ndigits[-1],ndigits[0:-1]
           r.append(MF.digit2num(ndigits))
   return r

count=0
for p in it.takewhile(lambda x:x<1000000,MF.primeiter()):
    for pr in rotation(p):
        if not MF.isprime(pr):
            break
    else:
        count+=1
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))

#opitimize rotation to avoiding using list
s2=time.clock()
def rotationiter(n):
    Length=len(str(n))
    yield n
    if Length>1:
        for k in range(Length-1):
            n=(n%10)*10**(Length-1)+n//10
            yield n

count=0
for p in it.takewhile(lambda x:x<1000000,MF.primeiter()):
    for pr in rotationiter(p):
        if not MF.isprime(pr):
            break
    else:
        count+=1
print(count)
print('After optimizing, runing time: {0}s'.format(round(time.clock()-s2,3)))