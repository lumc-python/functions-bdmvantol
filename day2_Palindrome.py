# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:11:50 2019

@author: Bianca
"""

def palindrome(a):
    for i in range(len(a)//2):
        if a[i] != a[len(a)-i-1]:
            return False
    return True 

print(palindrome('effe'))
print(palindrome(str(1001)))
print(palindrome(str(1234)))
print(palindrome('hallo'))

def palindrome2(a):
    if a[:] != a[::-1]:
        return False
    return True 

print(palindrome2('effe'))
print(palindrome2(str(1001)))
print(palindrome2(str(1234)))
print(palindrome2('hallo'))

def palindrome3(a):
    return a[:] == a[::-1]
     
print(palindrome3('effe'))
print(palindrome3(str(1001)))
print(palindrome3(str(1234)))
print(palindrome3('hallo'))