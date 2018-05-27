# -*- coding: utf-8 -*-
"""
Created on Sat May 26 23:22:32 2018

@author: JPBDell
"""

import math
tally = 0

num = str(math.factorial(100))
for i in num:
    tally += int(i)
    
print(tally)
    