# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:45:15 2017

@author: Tsui
"""

'''
Method 1
From 40 Movements choosing 20 ones for downwards
Just a simple combination problem.
time:0.0006s
'''
import time
s=time.clock()
import math
def nchoosek(n,k):
    den=math.factorial(k)*math.factorial(n-k)
    num=math.factorial(n)
    return num//den

print(nchoosek(40,20))
print('Runing time: {0}s'.format(round(time.clock()-s,4)))

'''
Method 2
Using the recurison function 'pathway()'
time:0.0126s
'''
s2=time.clock()
step_dict={}
def pathway(right,down):
    steps=0
    if (right,down) in step_dict:
        steps=step_dict[(right,down)]
    elif  down==1 or right==1:
        steps=1
    else:
        for i in range(down):
            step_dict[(right-1,down-i)]=pathway(right-1,down-i)
            steps+=step_dict[(right-1,down-i)]
    return steps

print(pathway(21,21))    
print('Runing time: {0}s'.format(round(time.clock()-s2,4)))