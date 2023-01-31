# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:54:40 2021

@author: Kubwi
"""

import numpy
import matplotlib.pyplot as plt
import random
import math
print('enter the number of rounds per simulation')

x=True
counter=0
while x is True:
    UserInput=input()
    for i in range(int(UserInput)):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        result=math.pow(x,2)+math.pow(y,2)
        Result=math.sqrt(result)
        if Result<=1:
            counter+=1
            plt.scatter(x,y)
            
        else:
            counter+=0
    pi=4*(counter/int(UserInput))
    print("pi is per ",UserInput,"per simulation",pi)
   
  
        