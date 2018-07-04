# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 21:21:07 2017

@author: Tsui
"""

a=sum([x**2 for x in range(1,101)])
b=sum(range(1,101))**2
print(abs(a-b))