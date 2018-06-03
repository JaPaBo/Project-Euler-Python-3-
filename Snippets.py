# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:25:49 2018

@author: JPBDell
"""


#########################################################################################
#Past at beginning of script to start computation timer
import time
start = time.time()

#paste at end of script to get computation time
elapsed = (time.time() - start)
print("elapsed time is: {} seconds".format(str(elapsed)))



########################################################################################
#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))