# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:30:35 2019

@author: Bianca
"""

def pos_neg(a):
    pos_count = 0
    neg_count = 0 
    
    for i in a:
        if i >= 0:
            pos_count = pos_count + 1
        else:
            neg_count = neg_count + 1
    print(pos_count)
    print(neg_count)

pos_neg([6,7,8,9,0,-1,-3,-4])    