# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:09:39 2017

@author: cq_xuke
"""

import time
s=time.time()
myfile=open(r'C:\Users\cq_xuke\EulerProjet\p022_names.txt')
strname=myfile.read()+','
x='';name=[]
for strs in strname:
    if strs is '"':
        continue
    x=x+strs
    if strs is ',':
        name.append(x[0:-1])
        x=''
name=sorted(name)
def namescores(index,Name):
    name_pos=[ord(asc)-ord('A')+1 for asc in Name]
    return index*sum(name_pos)

count=0
for i in range(len(name)):
    count+=namescores(i+1,name[i])
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,4)))