# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:46:33 2017

@author: Tsui
"""

term1=1;term2=1;count=2
while term1+term2<=4000000:
    term=term1+term2
    if term%2==0:
        count+=term
    term1,term2=term2,term
print(count)