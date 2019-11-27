# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:38:49 2019

@author: Bianca
"""

def transform(a):
    
    Pos_value = False 
    for i in range(len(a)):
        if a[i] > 0:
            a[i] = a[i] * -1
            Pos_value = True
#    print(a)
    return Pos_value
    
print(transform([-5,-4,-3,-2,-1,0,1,2,3,4,5]))
print(transform([-5,-4,-3,-2,-1,0,-1,-2,-3,-4,-5]))    