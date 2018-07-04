# -*- coding: utf-8 -*-
import sympy
from math import floor, ceil
import numpy as np
from operator import methodcaller

class polygonal:
    def __init__(self, min_, max_):
        self._n = sympy.Symbol('n')
        self._min = min_
        self._max = max_


    def triangle(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n*(n+1)/2-self._min, n)))
        max_n = floor(max(sympy.solve(n*(n+1)/2-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n*(n+1)//2


    def square(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n**2-self._min, n)))
        max_n = floor(max(sympy.solve(n**2-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n**2


    def pentagonal(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n*(3*n-1)/2-self._min, n)))
        max_n = floor(max(sympy.solve(n*(3*n-1)/2-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n*(3*n-1)//2
    

    def hexagonal(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n*(2*n-1)-self._min, n)))
        max_n = floor(max(sympy.solve(n*(2*n-1)-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n*(2*n-1)


    def heptagonal(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n*(5*n-3)/2-self._min, n)))
        max_n = floor(max(sympy.solve(n*(5*n-3)/2-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n*(5*n-3)//2


    def octagonal(self):
        n = self._n
        min_n = ceil(max(sympy.solve(n*(3*n-2)-self._min, n)))
        max_n = floor(max(sympy.solve(n*(3*n-2)-self._max, n)))
        for n in range(min_n, max_n+1):
            yield n*(3*n-2)
    

    def __call__(self):
        methods = [method for method in dir(polygonal)
                   if not method.startswith('__')]
        return [methodcaller(method)(self) for method in methods]
        

array = polygonal(1000, 9999)()
seq = []


def find_chain(n, polygonal):
    global seq
    n = str(n)
    seq.append(n)
    for i in range(len(polygonal)):
        candidates = [str(num) for num in polygonal[i]
                      if str(num).startswith(n[2:])]
        print(candidates)###
        if candidates != []:
            for num in candidates:
                temp = polygonal
                temp.pop(i)
                find_chain(num, temp)
        if len(seq) != 6:
            seq = []
        else:
            return seq
    else:
        print("没有结果")
        
    
    
    
    






