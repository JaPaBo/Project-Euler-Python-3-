# -*- coding: utf-8 -*-
"""
Solve Project Euler Problem 11 by importing from csv
"""
import csv
import numpy as np
import time
 
start = time.time()
NumLin = 4 #quantity of numers in a row to use for product 
MaxHorizontal = 0
MaxVertical = 0
MaxBackSlash = 0
MaxForwardSlash = 0
MaxProduct = 0 #record of highest product observed

NumArray = np.genfromtxt('Prob11.csv', delimiter=' ') #NumArray is a list of i rows; rows are a list of j cells



#Iterate horizontal
for i in range(len(NumArray)):
    for j in range(len(NumArray[i])-NumLin+1):
        LocalValue = 1
        for k in range(NumLin):
            LocalValue *= NumArray[i][j+k]
        MaxHorizontal = max(MaxHorizontal, LocalValue)
        #print("Horizontal local %f, max %f" % (LocalValue, MaxProduct))


#Iterate Vertical

for i in range(len(NumArray)-NumLin+1):
    for j in range(len(NumArray[i])):
        LocalValue = 1
        for k in range(NumLin):
            LocalValue *= NumArray[i+k][j]
        MaxVertical = max(MaxVertical, LocalValue)
        #print("Vertical local %f, max %f" % (LocalValue, MaxProduct))
        
    
#Iterate diagonal, down and right (Backslash)
for i in range(len(NumArray)-NumLin+1):
    for j in range(len(NumArray[i])-NumLin+1):
        LocalValue = 1
        for k in range(NumLin):
            LocalValue *= NumArray[i+k][j+k]
        MaxBackSlash = max(MaxBackSlash, LocalValue)
        #print("Diagonal local %f, max %f" % (LocalValue, MaxProduct))
        
#Iterate diagonal, up and right (Forward Slash)
for i in range(len(NumArray)-NumLin+1):
    for j in range(len(NumArray[i])-NumLin+1):
        LocalValue = 1
        for k in range(NumLin):
            LocalValue *= NumArray[i-k+NumLin-1][j+k]
        MaxForwardSlash = max(MaxForwardSlash, LocalValue)
        #print("Diagonal local %f, max %f" % (LocalValue, MaxProduct))

#Find maximum of horizontal, vertical, diagonal
MaxProduct = max(MaxHorizontal, MaxVertical, MaxBackSlash, MaxForwardSlash)
elapsed = (time.time() - start)
 
print("%s found in %s seconds" % (MaxProduct,elapsed))