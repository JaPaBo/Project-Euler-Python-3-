# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:29:37 2018

@author: JPBDell
"""
import math
import time
num_consecutive = 13
max_product = 0

#read csv file
start = time.time()
with open ("Prob8.csv", "r") as myfile:
    data=myfile.readlines()


#Convert input from csv file to single large string containing all characters
#in originally read order.  Stripping "\n" characters
big_string = ""
for i in data:
    big_string += i.strip("\n")
#print(big_string)


#Determine largest product of num_consecutive integers in max_product
for i in range(len(big_string)-num_consecutive+1):
    product = 1
    for j in range(num_consecutive):
        product *= int(big_string[i+j])
    max_product = max(product, max_product)
    #print(i)
    
    
elapsed = (time.time() - start)
print("Max product of {} integers is: {}\nElapsed time: {}".format(num_consecutive,max_product,elapsed))
