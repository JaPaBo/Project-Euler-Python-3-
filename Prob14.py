# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
start = time.time()

#numbar = 20
chain = [0,0] #[number, sequence]
cap = 1000000 #max number to go to

def collatz(numbar):
    if numbar%2:
        numbar *= 3
        numbar += 1
    else:
        numbar /= 2
    return numbar
        
for i in range(2,cap):
    count = 0
    num = i
    while num != 1:
        num = collatz(num)
        count += 1
    if count > chain[1]:
        chain = [i,count]

elapsed = (time.time() - start)
print("Answer is: {}.  Chain Length was: {}.  Elapsed time is: {} seconds".format(chain[0],chain[1],elapsed))