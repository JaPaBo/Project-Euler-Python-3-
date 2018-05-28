# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
 
start = time.time()

n = 100000
number = 600851475143
maxprimefactor = 0

def prime_gen(n):
    #modified from https://stackoverflow.com/questions/29812602/basic-prime-number-generator-in-python
    primes = [2]
    a = 2 
    while a < n:
        counter = 0 
        for i in primes:
            if a % i == 0:
                counter += 1
        if counter == 0:
            primes.append(a)
        else:
            counter = 0
        a = a + 1

    print(primes)
    return primes
 
primes = prime_gen(n)

for i in primes:
    if number%i == 0:
        print(i)
        #print("/n")
        maxprimefactor = max(maxprimefactor, i)

elapsed = (time.time() - start)
print(elapsed)
print("max prime factor is: %s" % str(maxprimefactor))