# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
 
start = time.time()

nth_prime = 10001


def nth_prime_gen(nth_prime):
    #modified from https://stackoverflow.com/questions/29812602/basic-prime-number-generator-in-python
    primes = [2]
    a = 2 
    while (len(primes) < nth_prime):
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
 
primes = nth_prime_gen(nth_prime)


elapsed = (time.time() - start)
print("{}th prime factor is: {}".format(str(nth_prime),str(primes[nth_prime-1])))
print("elapsed time is: {} seconds".format(str(elapsed)))