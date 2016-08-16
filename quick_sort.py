# -*- coding: utf-8 -*-
"""
quick sort 
Created on Tue Aug 16 17:40:24 2016

@author: Lucy
"""


    

def quick(lst,bp,ep):
    if bp<ep:  
        #partition 
        pivot = lst[bp]
        left = bp + 1
        right = ep
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
        lst[bp], lst[right] = lst[right], lst[bp]
            
       
        
        print(str(lst))
        quick(lst,bp,right-1)
        quick(lst,right+1,ep)
        
    
lst = [5,8,2,1,9,3,4,7]
quick(lst,0,len(lst)-1)
print(lst)
