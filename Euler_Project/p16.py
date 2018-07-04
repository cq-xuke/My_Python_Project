# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 12:27:02 2017

@author: Tsui
"""

import time
from MyModules.MyFunction import num2digit
s=time.clock()
digits=num2digit(2**1000)
print(sum(digits))
print('Runing time: {0}s'.format(round(time.clock()-s,4)))