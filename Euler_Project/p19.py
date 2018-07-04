# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 19:57:06 2017

@author: Tsui
"""

import time
s=time.time()
count=0
for Year in range(1901,2001):
    if Year % 4 == 0:
        yearday=366
    else:
        yearday=365
    for day in range(1,yearday+1):
        date=time.strptime('{0} {1}'.format(Year,day),'%Y %j')
        if date[2]==1 and date[6]==6:
            count+=1
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,3)))