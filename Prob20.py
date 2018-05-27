# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:22:32 2018

@author: JPBDell
"""

import math
import time
 
start = time.time()
tally = 0

num = str(math.factorial(100))
for i in num:
    tally += int(i)
print("start!")

elapsed = (time.time() - start)
print("Solution is %i.  Calculated in %f seconds" % (tally, elapsed))