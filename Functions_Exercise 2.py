# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:40:32 2019

@author: Bianca
"""
def max(number1, number2):
    if number1 > number2:
        return number1
    else: 
        return number2


def max3(number1, number2, number3):
    return max(max(number1,number2),number3)   
    

#def max3(number1, number2, number3):
#    if number1 > number2 and number1 > number3:
#        print(number1)
#    elif number2 > number3:
#        print(number2)
#    else:
#        print(number3)
   
print(max3(3,1,5))     
