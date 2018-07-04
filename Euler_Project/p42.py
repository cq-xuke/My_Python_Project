# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:35:48 2017

@author: cq_xuke
"""

import time
s=time.clock()
myfile=open(r'C:\Users\cq_xuke\EulerProjet\p042_words.txt')
name=myfile.read().replace('"','').split(',')
myfile.close()
def istriangle(n):
    nt=((1+8*n)**0.5-1)*0.5
    flag=False
    if nt==int(nt):
        flag=True
    return flag

def wordvalue(w):
    return sum(map(lambda x:ord(x)-64,w))

count=0
for na in name:
    if istriangle(wordvalue(na)):
        count+=1
print(count)
print('Runing time: {0}s'.format(round(time.clock()-s,3)))