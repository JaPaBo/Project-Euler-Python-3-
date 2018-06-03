# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:15:06 2018

@author: JPBDell
"""

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
    
    
coolness = factors(28)
