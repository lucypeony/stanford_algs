# -*- coding: utf-8 -*-
"""
“You are given as input an unsorted array 
of n distinct numbers, where n is a power of 2.
 Give an algorithm that identifies the second-largest 
 number in the array, and that uses at most n+log2n−2 comparisons.”

Created on Thu Aug 11 10:07:05 2016

@author: Lucy
"""

#This one uses at most 2n comparisons 
def second_largest(my_list):
    first, second = 0,0
    for i in range(len(my_list)):
        if second < my_list[i]:
            if first < my_list[i]:
                second = first
                first = my_list[i]
                
            else:
                second = my_list[i]
    
    return second 


   
#loser tree solution 
#First we have a function for fast max search in array with n-1 comparisons. This function also returns the list of all potential second maxes.

#Calculate the max and potential second maxes on the left half of array
#Calculate the max and potential second maxes on the right half of array
#if max_left > max_right, then return max_left and left_second_maxes with max_right added, otherwise return max_right and right_second_maxes with max_left added
#Then we call this function in main function two times

#We call the function on whole array and it returns max value and \log_2{n} of potentials by doing n-1 comparisons
#We call the function on potential second maxes and it uses \log_2{n} -1 comparisons, and return the max value returned from this call


def loser_tree(my_list):
    res =[]
    if len(my_list)==1:
        res.append(my_list[0])
        return my_list[0],res
    elif len(my_list)==2:
        temp_max=0
        temp_min=0
        if my_list[0]>my_list[1]:
            temp_max=my_list[0]
            temp_min=my_list[1]
        else:
            temp_max=my_list[1]
            temp_min=my_list[0]
        
        res.append(temp_min)
        return temp_max, res
        
        
    mid = len(my_list) // 2
    max_left,second_max1 = loser_tree(my_list[: mid])
    max_right, second_max2 = loser_tree(my_list[mid :])
    if max_left > max_right :
        second_max1.append(max_right)
        return max_left, second_max1
    else:
        second_max2.append(max_left)
        return max_right, second_max2
        
def loser_fun(my_list):
    
    #calcaute the max , and the loser list 
    max_list, loser_list= loser_tree(my_list)
    
    #get the max of the loser list 
    second_max,ulist = loser_tree(loser_list)
    return second_max
    
    
my_list = [1,2,9,8,3,4,5,100,1001]
print(second_largest(my_list))

print(loser_fun(my_list))
                