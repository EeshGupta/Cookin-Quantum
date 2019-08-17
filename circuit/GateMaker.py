# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:40:17 2019

@author: Eesh Gupta
"""
import numpy as np
import math
import cmath

class gateMaker(object): 
    def __init__(self, alpha, theta, beta, gamma): 
        """
        Input: angles alpha, theta, beta and gamma
        direction of unit axis. 
        """
        self.alpha = alpha
        self.beta = beta
        self.theta = theta
        self.gamma = gamma
    
    @property
    def X(self): 
        """
        Output: Pauli X gate for a single qubit
        """
        return np.array([[0, 1], [1, 0]])
    
    @property
    def Y(self): 
        """
        Output: Pauli Y gate for a single qubit
        """
        return np.array([[0, -complex(0,1)], [complex(0,1), 0]])
    
    @property
    def Z(self): 
        """
        Output: Pauli Z gate for a single qubit
        """
        return np.array([[1, 0], [0, -1]])
    
    @property
    def I(self): 
        """
        Output: Identity gate for a single qubit
        """
        return np.array([[1, 0], [0, 1]])
    
    def R(self, axis, angle): 
        """
        Input: A pauli gate as axis to specify around which axis the 
        rotation op to be constructed and the angle
        Output: Rotation operator around the specified axis
        """
        return ((math.cos(angle/2))*(self.I)) - ((complex(0,1))*(math.sin(angle/2))*(self.axis))
    
    
    def make(self): 
        """
        Output: A single qubit gate as a composition of the pauli gates
        """
        return (math.e**(complex(0,1)*self.alpha))*self.R(self.beta, self.Z)*self.R(self.gamma, self.Y)*self.R(self.theta, self.Z)
        