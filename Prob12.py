# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time

answer = []
factors = []
i = 2
new = 0
triangle = [1]
latch = 0


from functools import reduce

def factor(n):    #https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
 
start = time.time()

while(len(factors)<500):
    new = triangle[len(triangle)-1]+i
    triangle.append(new)
    count = 0
    factors = []
    
    ''' #My solution to determine factors was undesirably slow, so substituted factor function from SE discussion
    for j in range(1,new//2):
        if new%j == 0:
            count +=1
            factors.append(j)
    factors.append(new)'''
    
    factors = factor(new)
    

    i += 1
#don't forget to include the new number itself...

elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))

