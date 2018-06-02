# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time

sum = 1000
 
start = time.time()

for ai in range(1,sum//3):
    for bi in range(ai+1,sum//2+1):
        ci = sum - ai - bi
        
        if abs((ai**2 + bi**2) - ci**2) == 0:
            print("{}     ai={} bi={} ci={}    ai**2+bi**2={} ci**2={}".format(ai*bi*ci,ai,bi,ci,ai**2+bi**2,ci**2))


elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))