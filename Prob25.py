# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
start = time.time()

fib_sequence = [2,1,1] #[n,Fn,Fn-1]
digits = 1000

def fib(list):
    #print("{}".format(list))
    return [(list[0]+1), (list[1]+list[2]), (list[1])]


while len(str(fib_sequence[1]))<digits:
    fib_sequence = fib(fib_sequence)

elapsed = (time.time() - start)
print("Answer is: {}.  Elapsed time is: {} seconds".format(fib_sequence[0],elapsed))