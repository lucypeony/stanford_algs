# -*- coding: utf-8 -*-
"""
quick sort 
Created on Tue Aug 16 17:40:24 2016

@author: Lucy
"""
import statistics


def quick_pq(lst,bp,ep):
    if bp<ep:
        
        """
        Median of Three method
        """
        
        first = lst[bp]
        final = lst[ep]
        med = (bp + ep) // 2
        median1 = lst[med]
        
        templst = [first, final, median1]
        temp = statistics.median(templst)
            
        pos = 0            
            
        if temp == first :
            pos = bp
        elif temp == final :
            pos = ep
        elif temp == median1 :
            pos = med
        
            
            
        lst[bp],lst[pos]=lst[pos],lst[bp]
            
        
        
        
        
        
        """
        to use the final element as pivot
        """        
        #lst[bp],lst[ep]=lst[ep],lst[bp]        
        #print("swap",str(lst))        
        
        #partition 
        #print(lst[bp:ep+1],bp,ep)
        pivot = lst[bp]
        i = bp
        j = i+1 
        while j <= ep :
            if lst[j]<pivot :
                
                i = i + 1
                lst[j],lst[i]=lst[i],lst[j]
            j = j + 1
        lst[i],lst[bp]= lst[bp], lst[i]
        
        #print("After Partition : ",str(lst[bp:ep+1]))
                
        #print(str(lst))
        res = ep - bp 
        res = res + quick_pq(lst,bp,i-1)
        res = res + quick_pq(lst,i+1,ep)
        #print(res,bp,ep)
        return res
    else:
        return 0




    

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
        
    
my_file = open("QuickSort.txt")
my_list = []
for line in my_file:
    my_list.append(int(line))


res = quick_pq(my_list,0,len(my_list)-1)
print(res)
print("the list")
print(my_list)
"""

lst = [4,3,2,1,-1,-9,10]
comp= quick_pq(lst, 0, len(lst) - 1)
print(str(lst),comp)

"""