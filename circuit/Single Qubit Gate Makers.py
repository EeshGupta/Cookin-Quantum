# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:40:17 2019

@author: Eesh Gupta
"""
import numpy as np
import math
import cmath

class singleQubitGateMaker1Axis(object): 
    """Decomposition of unitary gate into 1 rotation operator """
    
    def __init__(self, alpha, theta, axis1): 
        """
        Input: Angle alpha for phase, angle theta for construction of rotation
        operator around axis1 (list of vector components).
        """
        self.alpha = alpha
        self.theta = theta
        self.axis1 = axis1
    
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
    
    def R(self, axis_vector, angle):
        """
        Input: Axis components in list form and angle in radians
        Output: A rotation operator
        """
        axis = (axis_vector[0]*self.X) + (axis_vector[1]*self.Y) + (axis_vector[2]*self.Z)
        
        return (math.cos(angle/2)*self.I) - complex(0,1)*(math.sin(angle/2))*(axis)
        
    def make(self): 
        """
        Output: A single qubit gate as a composition of the pauli rotation
        operators
        """
        return (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
               self.theta)

class singleQubitGateMaker2Axes(object):
    """Decomposition of unitary gate into 2 rotaion operators
    (eg. XY and ZY)"""
    
    def __init__(self, alpha, beta, gamma, delta, axis1, axis2): 
        """
        Input: Angle alpha for phase, angles beta and delta for contruction of 
        respective rotation operators around axis1 (list of vector components), 
        angle gamma for construction of rotation operator around axis2 
        (list of vector components).
        """
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.axis1 = axis1
        self.axis2 = axis2
    
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
    
    def R(self, axis_vector, angle):
        """
        Input: Axis components in list form and angle in radians
        Output: A rotation operator
        """
        axis = (axis_vector[0]*self.X) + (axis_vector[1]*self.Y) + (axis_vector[2]*self.Z)
        
        return (math.cos(angle/2)*self.I) - complex(0,1)*(math.sin(angle/2))*(axis)
        
    def make(self): 
        """
        Output: A single qubit gate as a composition of the pauli gates
        """
        return (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
               self.beta)*self.R(self.axis2, self.gamma)*self.R(self.axis1, 
                                self.delta)
