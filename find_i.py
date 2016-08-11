# -*- coding: utf-8 -*-
"""
“You are given a sorted (from smallest to largest) array A 
of n distinct integers which can be positive, negative,
 or zero. You want to decide whether or not there is 
 an index i such that A[i] = i. Design the fastest 
 algorithm that you can for solving this problem.”

Created on Thu Aug 11 12:47:56 2016

@author: Lucy
"""

def find_i(lst,bp,ep):
    """ To find the A[i]=i"""
    #leng = len(lst)
    
    if bp>= ep :
        return -1
    
    res = None
    
    mid = len(lst) //2
    mp = mid + bp
    print(bp,mp,ep,mid,lst[mid])
    if lst[mid] > mp :
        res =find_i(lst[: mid],bp,mp)
    elif lst[mid] < mp :
        res =find_i(lst[mid :],mp,ep)
    else :
        res=mp
        return mp
    return res  
    
lst =[-10,-2,-1,0,4,9,10]
print(find_i(lst,0,6))