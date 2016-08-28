# -*- coding: utf-8 -*-
"""
Stanford Week3 
Randomized Selection

Created on Sun Aug 28 20:34:26 2016

@author: Lucy
"""

import random 

def random_median(lst,target):
    
    rand_index = random.randint(0,len(lst)-1)
    pivot = lst[rand_index]
    print(lst,target,pivot)    
    
    #partition :
    #those less than pivot --> right
    #those more than pivot --> left 
    lst[0],lst[rand_index] = lst[rand_index], lst[0]
    left = 1
    right = len(lst) -1 
    Done = False
    while not Done:
        if left <=right and lst[left]<=pivot:
            left = left + 1
        if right >= left and lst[right]>=pivot :
            right = right - 1
        if left > right :
            Done=True
        else:
            lst[left],lst[right] =lst[right],lst[left]
    lst[0], lst[right] = lst[right], lst[0]
    
    if right > target :
        return random_median(lst[:right],target)
    elif right < target:
        return random_median(lst[right:],target - right)
    else:
        return lst[right]
    
    
lst = [10,9,8,7,6,5,4,3,2,1,0]
lst_median = random_median(lst,2)
print(lst_median)


