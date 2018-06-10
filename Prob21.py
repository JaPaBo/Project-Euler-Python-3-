# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:22:32 2018

@author: JPBDell
"""

import math
import time
 
start = time.time()
amicable_numbers = []

def divisors(numbar):
    divisors = []
    for i in range(1,numbar//2+1):
        if numbar%i == 0:
            divisors.append(i)
    return divisors

def divisors_sum(numbar):
    divisorz = divisors(numbar)
    sum = 0
    for i in divisorz:
        sum += i
    return sum
      

##############################################################################
##### MAIN CODE ##############################################################
    ##########################################################################
for i in range(1,10001):
    candidate = divisors_sum(i)
    if ((divisors_sum(candidate) == i)&(candidate != i)):   #Verifying that (1) sums of divisors match and (2) a != b 
        amicable_numbers.append(i)

print(amicable_numbers)
amicable_sum = 0
for i in amicable_numbers:
    amicable_sum += i
    
elapsed = (time.time() - start)
print("Solution is {}.  Calculated in {} seconds".format(amicable_sum, elapsed))