# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:22:32 2018

@author: JPBDell
"""

import math
import time
biggest = 0

start = time.time()

for i in range(1,math.factorial(20)+1):
    modulus = 0
    for j in range(2,21):
        if i%j != 0:
            modulus += 1
    if modulus == 0:
        biggest = i
        break

elapsed = (time.time() - start)

print("Solution is %i.  Calculated in %f seconds" % (biggest, elapsed))