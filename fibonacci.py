#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 19:35:08 2018

@author: kash-py
"""



#kash-py

#fibonacci sequence 
#each number in the sequnce is the sum of the previous two

#this program computes n/th fibonacci number \
#where n is number supplied by the user


fib_num = int(input('Please type in a number: '))
#print(type(fib_num))

def fib(n):
    #pass
    fib = 1
    num = 0
    for i in range(n-1):
        fib , num = fib + num , fib    
    
    
    print('Fibonacci Number For {0} is : {1}'.format(n , fib))
    
    
#############Examples################
# =============================================================================
#     
# fib(fib_num)
# 
# 
# for i in range(19,23):
#     fib(i)
#     
#     
# =============================================================================
    