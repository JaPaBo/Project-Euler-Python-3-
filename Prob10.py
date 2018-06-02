# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
 
start = time.time()

sum = 0


def nth_prime_gen(nth_prime):
    #modified from https://stackoverflow.com/questions/29812602/basic-prime-number-generator-in-python
    primes = [2]
    a = 2 
    while (1):
        counter = 0 
        for i in primes:
            if a % i == 0:
                counter += 1
                break #adding this break statement reduced execution time by an order of magnitude
        if counter == 0:
            primes.append(a)
        else:
            counter = 0
        if a == 2000000:
            break
        a = a + 1

    print(primes)
    return primes
 
primes = nth_prime_gen(nth_prime)
for i in primes:
    sum += i
    
print(sum)
elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))