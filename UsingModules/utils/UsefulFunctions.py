# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:53:32 2021

@author: hreed
"""

import numpy as np
import matplotlib.pyplot as plt

def plot(y, x):
    plt.plot(y, x)
    plt.title("Plot")
    plt.show()
    
def say_hi():
    print('Hi!')
    
def example_return(x):
    plt.plot(x, 5*x)
    plt.title("5x")
    plt.show()
    return 5*x