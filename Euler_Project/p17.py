# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:34:12 2017

@author: Tsui
"""

import time
s=time.clock()
def countnum(num):
    if num==0:
        n=0
    k1=[1,2,6,10];k2=[4,5,9]
    k3=[3,7,8];k4=[11,12]
    k5=[15,16];k6=[13,14,18,19]
    k7=[20,30,80,90];k8=[40,50,60]
    k9=[70];k10=[17]
    if num in k1:n=3
    elif num in k2:n=4
    elif num in k3:n=5
    elif num in k4:n=6
    elif num in k5:n=7
    elif num in k6:n=8
    elif num in k7:n=6
    elif num in k8:n=5
    elif num in k9:n=7
    elif num in k10:n=9
    n1=0;n2=0
    if 20<num<100:
        C1=num-num%10;C2=num%10
        if  C1 in k7:n1=6
        elif C1 in k8:n1=5
        elif C1 in k9:n1=7
        if C2 in k1:n2=3
        elif C2 in k2:n2=4
        elif C2 in k3:n2=5
        elif C2 in k4:n2=6
        elif C2 in k5:n2=7
        elif C2 in k6:n2=8
        return n1+n2
    return n

n=1;count=0
for i in range(1,100):
    count+=countnum(i)
for i in range(100,1000):
    n1=i//100
    n2=i-n1*100
    if i % 100 ==0:
        count+=countnum(n1)+len('hundred')
    else:
        count+=countnum(n1)+countnum(n2)+len('and')+len('hundred')
print(count+len('onethousand'))
print('Runing time: {0}s'.format(round(time.clock()-s,4)))