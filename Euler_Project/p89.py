# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:10:59 2018

@author: cq_xuke
"""

def alabo2_num(one_num):  
    ''''' 
    将阿拉伯数字转化为罗马数字 
    '''  
    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  
    res=''  
    for i in range(len(num_list)):  
        while one_num>=num_list[i]:  
            one_num-=num_list[i]  
            res+=str_list[i]  
    return res  
  
  
def roman2_alabo(one_str):  
    ''''' 
    将罗马数字转化为阿拉伯数字 
    '''  
    define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  
    if one_str=='0':  
        return 0  
    else:  
        res=0  
        for i in range(0,len(one_str)):  
            if i==0 or define_dict[one_str[i]]<=define_dict[one_str[i-1]]:  
                res+=define_dict[one_str[i]]  
            else:  
                res+=define_dict[one_str[i]]-2*define_dict[one_str[i-1]]  
        return res


def main():
    with open(r'C:\Users\cq_xuke\Desktop\temp\p89.txt', 'r') as f_89:
        romans = [roman.strip('\n') for roman in f_89.readlines()]
        nums = [roman2_alabo(roman) for roman in romans]
        romans_modified = [alabo2_num(num) for num in nums]
        diff = sum([len(roman)-len(roman_d)
                    for (roman, roman_d) in zip(romans, romans_modified)])
    return diff


if __name__ == '__main__':
    print(main())