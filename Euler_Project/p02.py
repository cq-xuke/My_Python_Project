# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:43:17 2017

@author: Tsui
"""

iseven=lambda a:bool(not a%2)
fdict={0:0,1:1,2:1}
i=2
while fdict[i]<=4000000:
    i+=1
    fdict[i]=fdict[i-1]+fdict[i-2]
fdict.pop(i)
f=filter(iseven,fdict.values())
print(sum(f))