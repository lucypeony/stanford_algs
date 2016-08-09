# -*- coding: utf-8 -*-
"""
Implement the Grade School Integer Mulitplication method 

Created on Tue Aug  9 16:45:11 2016

@author: Lucy
"""

# grade School Integer Mulitipliation method 
def grade_school(x, y):
    # how many digits x have 
    x_list = list(map(int, str(x)))
    x_len = len(x_list)
    # how many digits y have 
    y_list = list(map(int, str(y)))
    y_len = len(y_list)
    
    # z used to store x*y 
    z_list = [0]*(x_len + y_len)
    #z_len = len(z_list)
    for i in range(0,y_len) :
        carry = 0
        for j in range(0,x_len):
            x_index = x_len - j -1
            y_index = y_len - i -1
            z_index = i + j
            temp = x_list[x_index] * y_list[y_index] + carry + z_list[z_index]
            carry = temp // 10
            temp = temp % 10
            z_list[z_index] = temp
            
            if x_index == 0:
                z_list[z_index + 1]=carry
          
    return z_list               


# Karatsuba Multiplication 
def karatsuba(x,y):
    if x in range(0,10) or y in range(0,10) :
        return x*y
    
    x_list = str(x)
    x_len = len(x_list)
    mid = x_len//2
    a = int(x_list[0: mid])
    b = int(x_list[mid: :])
    x_base=x_len - mid
    
    y_list = str(y)
    y_len = len(y_list)
    mid = y_len//2
    c = int(y_list[0: mid])
    d = int(y_list[mid ::])
    y_base = y_len - mid
    
    return karatsuba(a,c)*(10**x_base)*(10**y_base) + karatsuba(b,d) + karatsuba(a,d)*(10**x_base) + karatsuba(b,c)*(10**y_base)

import time

start = time.clock()
print(grade_school(12300000,2900))
end=time.clock()
print(end-start)


start = time.clock()
print(karatsuba(12300000,2900))
end=time.clock()
print(end-start)
    