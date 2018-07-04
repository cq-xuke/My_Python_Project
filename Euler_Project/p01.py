# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:32:33 2017

@author: Tsui
"""

m3m5=lambda a:bool(not a%3 or not a%5)
print(sum(filter(m3m5,range(1,1000))))