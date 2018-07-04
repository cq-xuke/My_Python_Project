# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:27:47 2017

@author: Tsui
"""

import time
from MyModules.MyFunction import divisor
s=time.time()
count=0
def realdivisor(n):
    return sorted(list(divisor(n)))[0:-1]
'''
注意到,在写divisor函数时返回的数据结构是集合,不是顺序表.
为了使用索引,用list()将集合转换成列表时,
不能保证此时该列表中元素有从小到大的排序.
(尽管从表面上看,原集合中的元素可能是顺序的,实际上各元素之间没有联系)
如: x={1,4,5,9,12,22,44,123,899}
    list(x)
    [1, 899, 4, 5, 9, 12, 44, 22, 123]
因此必须用sorted将列表排序,再删除列表最后一个元素即n本身.
一个有趣的现象是若集合元素之间间距较小,且相互相差不大的情况下
        list({1,2,3,4,5,6,7,8,9})
往往能得到正确的顺序：
        [1,2,3,4,5,6,7,8,9]
但 list({122,155,676756465})
   [676756465, 122, 155]
这个问题待学完数据结构后再来思考
'''
for a in range(1,10000):
    b=sum(realdivisor(a))
    if a==b:
        continue
    if sum(realdivisor(b))==a:
        count+=a
print(count)
print('Runing time: {0}s'.format(round(time.time()-s,4)))