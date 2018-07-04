# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:15:23 2017

@author: Tsui
"""

best=0;i=0
for a in range(100,1000):
    for b in range(a,1000):
        ab=a*b
        if ab<=best:
            break
        abstr=str(ab)
        if abstr==abstr[-1::-1]:
            best=int(ab)
print(best)