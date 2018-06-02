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

#establishing largest number of digits that can have an exponential sum larger than the number
for n in range(1,25): #25 is an arbitrarily big number expected to definitely exceed max number of digits of interest
    string = ""
    for char in range(n):
        string += "9"
    #print(string)
    if latch == 0:
        if ((n)*math.pow(9,5) < int(string)):
            print("max is {}".format(str(n-1)))
            latch = n #Number of digits in largest decimal number where sum of factorials can exceed number

    
for i in range(1000000):
    exponent_sum=0
    for j in str(i):
        exponent_sum += math.pow(int(j),5)
    if exponent_sum == i:
        answer.append(i)
    
for i in answer:
    answer[0] += i
#1 is removed based on problem statement
answer[0] -= 1

elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))
print("answer is: {}".format(answer[0]))
