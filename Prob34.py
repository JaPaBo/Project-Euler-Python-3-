# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time

answer = []
latch = 0

 
start = time.time()

for n in range(1,25):
    string = ""
    for char in range(n):
        string += "9"
    print(string)
    if latch == 0:
        if ((n)*math.factorial(9) < int(string)):
            print("max is {}".format(str(n-1)))
            latch = n-1 #Number of digits in largest decimal number where sum of factorials can exceed number

    
for i in range(1000000):
    factorial_sum=0
    for j in str(i):
        factorial_sum += math.factorial(int(j))
        if factorial_sum == i:
            answer.append(i)
            

elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))