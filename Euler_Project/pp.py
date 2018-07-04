# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 18:34:45 2018

@author: cq_xuke
"""

from MyModules.MyFunction import isprime
import time
from tqdm import tqdm

s=time.clock()

def prime_iterator(n):
    if n <= 1:
        yield None
    else:
        yield 2
        for num in range(3, n+1, 2):
            if isprime(num):
                yield num


def istrunc(num):
    while num > 10:
        dsum = sum(map(int, str(num)))
        if num % dsum != 0:
            return False
        num = num // 10
    return True


def isstrong(num):
    dsum = sum(map(int, str(num)))
    s, y = divmod(num, dsum)
    if y == 0 and isprime(s):
        return True
    return False


count = 0

valid = dict.fromkeys([str(n) for n in range(10000, 100000) if istrunc(n)], True)

for prime in tqdm(prime_iterator(10000000)):
    if prime < 10:
        continue
    if prime > 100000:
        if not valid.get(str(prime)[:4]):
            continue
    if isstrong(truncted) and istrunc(truncted):
        count += prime

print(count)

s=time.clock()
