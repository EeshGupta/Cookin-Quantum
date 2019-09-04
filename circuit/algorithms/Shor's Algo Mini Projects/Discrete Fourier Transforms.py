# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:17:40 2019

@author: Eesh Gupta
"""
import numpy as np
import math

#Normal Fourier Transform
def VandermondeBuilder(n): 
    """
    Input: int n
    Output: Vandermonde Matrix
    """
    #Initializing Matrix
    v_matrix = np.array([])
    list_var = []
    for i in range(n): 
        list_var.append(complex(0,0))
    for i in range(n): 
        v_matrix = np.append(v_matrix, list_var)
    v_matrix = np.reshape(v_matrix, (n,n))
    #Exponential
    w = math.e**((2*math.pi*complex(0,1))/n)
    #Bulk Work
    for i in range(n): 
        for j in range(n): 
            v_matrix[i,j] = w**(i*j)
            print(v_matrix[i,j])
    return v_matrix

def Transform(a, n): 
    """
    Input: a array vector with n components
    Output: array discrete fourier transform of a
    """
    return np.dot(VandermondeBuilder(n = n), a)
##### Creating FFT

def binaryw(n, w = None, dicty = None): 
    """
    Input: int n is a power of 2
    Output: 
    """
    if n == 1: 
        dicty[0] = w
    else: 
        if w == None: 
            w = math.e**((2*math.pi*complex(0,1))/n)
            dicty = {}
        dicty = binaryw(n/2, w, dicty)
        for i in range 
        
        