# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
start = time.time()

summation = 0
for i in str(2**1000): summation += int(i)


elapsed = (time.time() - start)
print("Answer is: {}.  Elapsed time is: {} seconds".format(summation,elapsed))