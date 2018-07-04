# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 18:30:53 2017

@author: Tsui
"""

def factor(n):
    from math import sqrt
    Factor=list()
    if n%2==0:
        while n%2==0:
            Factor.append(2)
            n=n//2
    factor=3
    maxfactor=sqrt(n)
    while n>1and factor<=maxfactor:
        if n%factor==0:
            while n%factor==0:
                Factor.append(factor)
                n=n//factor
            maxfactor=sqrt(n)
        factor+=2
    else:
        Factor.append(n)
    return Factor

print(factor(600851475143)[-1])