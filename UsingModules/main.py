# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:52:51 2021

@author: hreed
"""
import numpy as np
from utils.UsefulFunctions import say_hi, plot, example_return
from utils.digDeeper.deep import something_else
from a_function import something


# This is a function from a file in the same directory
something()

# Here are the function from the file "UsefulFunctions" in the file "Utils"
say_hi()

#crearting some input for the following functions
table = np.array([[1,2,3,4,5], [1,4,1,3,2]])

plot(table[0], table[1])

fivex = example_return(table[0])

# Here is the function from the file "deep" in the file "digDeeped" in "utils"
something_else()


