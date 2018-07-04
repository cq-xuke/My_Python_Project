#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import time
from math import factorial
s=time.clock()

def num2digit(n):
    return list(map(int,str(n)))

print(sum(num2digit(factorial(100))))
print('Runing time: {0}s'.format(round(time.clock()-s,4)))