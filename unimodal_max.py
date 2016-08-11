# -*- coding: utf-8 -*-
"""
“You are a given a unimodal array of n distinct elements,
 meaning that its entries are in increasing order up 
 until its maximum element, after which its elements are
 in decreasing order. Give an algorithm to compute the 
 maximum element that runs in O(log n) time.”


Created on Thu Aug 11 11:32:15 2016

@author: Lucy
"""
#import math

def divide_conquer(my_list):
    #base case
    my_len = len(my_list)
    if my_len <=2 :
        return max(my_list)
    
    
    last = my_len -1 
    res = 0
    
    mid = len(my_list) // 2
    res1 =divide_conquer(my_list[: mid])
    res2 =divide_conquer(my_list[mid :])  
    res =max(res1,res2)    
    
    return res
  
  
def LimitedPeekFinding(lst):
  """lst should be firstly non-decreasing and then non-increasing"""
  n = len(lst)
  pos, key = n//2, lst[n//2]
  if pos > 0 and key < lst[pos-1]: return LimitedPeekFinding(lst[:pos])
  elif pos < (n-1) and key < lst[pos+1]: return LimitedPeekFinding(lst[pos+1:])
  else: return key

print(LimitedPeekFinding(list(map(int, input().split()))))  
  
  

my_list=[1,2,3,4,5,10,9,7,6]
print(divide_conquer(my_list))  
