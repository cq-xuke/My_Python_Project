# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:04:31 2017

@author: Tsui
"""

from functools import lru_cache
import time
s=time.clock()
def max_collatz():
    count = 1
    cache = dict()
    def collatz(n):
        nonlocal count, cache
        if n == 1:
            count_ = count
            count = 1
            return count_
        else:
            count += 1
            if n % 2 == 0:
                if collatz(n//2) <= 1000000:
                    cache[n//2] = collatz(n//2)
                return collatz(n//2)
            else:
                if collatz(n*3+1) <= 1000000:
                    cache[n*3+1] = collatz(n*3+1)
                return collatz(n*3+1)
    max_c = 0
    best_n = 0
    for i in range(1,1000001):
        if cache.get(i):
            co = cache[i]
        else:
            co = collatz(i)
        if co > max_c:
            max_c = co
            best_n = i
    return best_n

if __name__ == '__main__':
    print(max_collatz())
    print('Runing time: {0}s'.format(round(time.clock()-s,2)))