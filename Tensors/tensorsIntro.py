# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:01:08 2021

@author: hreed
"""

import numpy as np


###############
# Broadcasting
###############

# These arrays have different dimensions
x = np.array([1., 2])
y = np.array([3])

# We can still calculate 
a = x + y
# as python will treat like [1, 2] + [3, 3]

########################
# Matrix Vector Product 
########################

A = np.array(range(6)).reshape(3,2)
b = A@x 
# still works as we treat this as the following: 
# A = 0 1   x = 1  2
#     2 3       1  2
#     4 5       1  2
# where we multiply element wise and then add the columns

# we can expand the dimensions of x 
xe = np.expand_dims(x,0)
# above, we add an axis to the tensor

# print(A*xe)
# print('we can sum over an axis!')
# print(np.sum(A * xe, axis = 0)) 
# axis 0 is rows and 1 is columns 

##############
# Tensors 
##############

# just like an array (just more dimensions)
x = np.arange(2*5*3).reshape(2,5,3)

# axis 0 is the layer
# axis 1 is the rows
# axis 2 is the column

y = np.ones((5, 4))

# Tensor contractions  (3 ways)

# we want to calculate: 
    # a[i,j,k] = sum_r x[i,r,k] * y[r,j]

# (1) tensordot #####################################
a = np.tensordot(x, y, [1,0]) # specify the axis which you are summing over
# print(a.shape)
# doing this, we have a[i,k,j] in the wrong order - so we fix
a = np.moveaxis(a, source = 2, destination = 1)
# print(a.shape)

# (2) Using einsum 'einstein summation' ##############
a = np.einsum('irk,rj->ijk', x, y) # just like line 60
print(a.shape)

# (3) Using broadcasting #############################
# you must expand the axis 
xe = np.expand_dims(x, axis = 2)
ye = y[np.newaxis, :, :, np.newaxis] #np.newaxis adds an axis there

a  = np.sum(xe*ye, axis = 1)
print(a.shape)
















