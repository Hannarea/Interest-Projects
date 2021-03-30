# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:52:51 2021

@author: hreed
"""
import numpy as np
from utils.UsefulFunctions import say_hi, plot, example_return
from a_function import something

say_hi()

table = np.array([[1,2,3,4,5], [1,4,1,3,2]])

plot(table[0], table[1])

fivex = example_return(table[0])

something()