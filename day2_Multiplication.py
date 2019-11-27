# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:59:33 2019

@author: Bianca
"""

def multiplication(a):
#    start_value = None
    

#    for i in a:
#        if i > 0:
#            start_value = i
#            print(i)
#            break
#    print(start_value)    
    
    result=1
    Pos_value = False
    for i in a:
        if i > 0:
            result = result * i
            Pos_value = True
            
    if Pos_value:
        return result
    
print(multiplication([-5,-4,-3,-2,-1,0,1,2,3,4,5]))
print(multiplication([-5,-4,-3,-2,-1,0,-1,-2,-3,-4,-5]))            