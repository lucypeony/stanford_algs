# -*- coding: utf-8 -*-
"""

Inversions Count
Given an array containing the numbes 1,2,3... in some arsitary order 
Output the number of inversions 
inversion means : number of pairs (i,j) of array ,where i<j & a[i]>a[j]

Created on Wed Aug 10 15:56:07 2016

@author: Lucy
"""
def merge_sort_count_inversions(arr):
    #l = len(arr)
    if len(arr) < 2:
        if len(arr)==1 :
            mysum =0
        if len(arr)==2 and arr[0]>arr[1]:
            mysum =1
        return arr, mysum 
    #print("arr length: ",len(arr))
    half = len(arr) // 2
    left,leftsum = merge_sort_count_inversions(arr[:half])
    right,rightsum  = merge_sort_count_inversions(arr[half:])
    splitsum = 0 
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
            splitsum += len(left)-li
            ri += 1
    mysum = rightsum + leftsum + splitsum
    #print("in merge_sort:",str(out))
    return out,mysum

my_file = open("count_inversions.txt")
my_list = []
for line in my_file:
    my_list.append(int(line))
print(merge_sort_count_inversions(my_list))  
