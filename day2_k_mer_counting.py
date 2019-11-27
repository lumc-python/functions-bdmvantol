# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:58:42 2019

@author: Bianca
"""

DNA = 'ACGT' * 3 + 'TTATT' * 5
print(DNA)
print(len(DNA))


def make_suffixs(string):
     for i in range(1, len(string)+1):
        print(string[i-1:])
        
make_suffixs(DNA)

def substrings_len_k(string,k):
    for i in range(0,len(string)+1-k):
        print(string[i:i+k])

substrings_len_k(DNA,3)

def substrings_len_k1(string,k=3):
    for i in range(0,len(string)+1-k):
        print(string[i:i+k])

substrings_len_k1(DNA,8)

def substrings_len_k2(string):
    k = 5
    for i in range(0,len(string)+1-k):
        print(string[i:i+k])

substrings_len_k2(DNA)

def unique_substrings(string,k=3):
    unique_substrings_var = set()
    for i in range(0,len(string)+1-k):
        unique_substrings_var.add(string[i:i+k])
    print(sorted(unique_substrings_var))

unique_substrings(DNA,3)