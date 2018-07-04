# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:51:49 2017

@author: cq_xuke
"""

import time
count=0
s=time.time()
for s1 in range(3):
    for s2 in range(5):
        for s3 in range(11):
            for s4 in range(21):
                if 10*s4+20*s3+50*s2+100*s1>200:
                    break
                for s5 in range(41):
                    for s6 in range(101):
                        for s7 in range(201):
                            p=s7+2*s6+5*s5+10*s4+20*s3+50*s2+100*s1
                            if p>200:
                                break
                            elif p==200:
                                count+=1
print(count+1)
print('Runing time: {0}s'.format(round(time.time()-s,2)))