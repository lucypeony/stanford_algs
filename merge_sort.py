# -*- coding: utf-8 -*-
"""
Stanford Algorithm Week 1 : Merge Sort
Created on Tue Aug  9 20:24:23 2016

@author: Lucy
"""

def merge_sort(arr):
    #l = len(arr)
    if len(arr) < 2:
        return arr
    print("arr length: ",len(arr))
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    out = []
    li = ri = 0  # index of next element from left, right halves
    while True:
        if li >= len(left):  # left half is exhausted
            out.extend(right[ri:])
            break
        if ri >= len(right): # right half is exhausted
            out.extend(left[li:])
            break
        if left[li] < right[ri]:
            out.append(left[li])
            li =li +  1
        else:
            out.append(right[ri])
            ri += 1
    print("in merge_sort:",str(out))
    return out
    
    
my_list=[9,8,7,5,4,3,2,1,11]    
print(str(merge_sort(my_list)))

    
    