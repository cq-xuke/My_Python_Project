# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:25:53 2017

@author: cq_xuke
"""

import time
s=time.clock()
from itertools import takewhile
def pentagon(init=None):
    if init is None:
        init=1
    while not ispentagon(init):
        init+=1
    n=((1+24*init)**0.5+1)//6
    while True:
        yield n*(3*n-1)//2
        n+=1

def ispentagon(n):
    flag=False
    if int(((1+24*n)**0.5+1)/6)==((1+24*n)**0.5+1)/6:
        flag=True
    return flag

flag=False
for p1 in pentagon(3):
    if flag==True:
        break
    for p2 in takewhile(lambda x:x<p1,pentagon(1)):
        if ispentagon(p1+p2) and ispentagon(p1-p2):
            print(int(p1-p2))
            flag=True
            break
print('Runing time: {0}s'.format(round(time.clock()-s,3)))