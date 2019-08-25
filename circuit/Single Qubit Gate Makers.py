# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:40:17 2019

@author: Eesh Gupta
"""



"""Archived """

#import numpy as np
#import math
#import cmath
#
#from GateMaker import gateMaker
#
#
#class singleQubitGateMaker1Axis(gateMaker): 
#    """Decomposition of unitary gate into 1 rotation operator """
#    
#    def __init__(self, alpha, theta, axis1): 
#        """
#        Input: Angle alpha for phase, angle theta for construction of rotation
#        operator around axis1 (list of vector components).
#        """
#        self.alpha = alpha
#        self.theta = theta
#        self.axis1 = axis1
#        
#    def make(self): 
#        """
#        Output: A single qubit gate as a composition of the pauli rotation
#        operators
#        """
#        return (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
#               self.theta)
#
#class singleQubitGateMaker2Axes(gateMaker):
#    """Decomposition of unitary gate into 2 rotaion operators
#    (eg. XY and ZY)"""
#    
#    def __init__(self, alpha, beta, gamma, delta, axis1, axis2): 
#        """
#        Input: Angle alpha for phase, angles beta and delta for contruction of 
#        respective rotation operators around axis1 (list of vector components), 
#        angle gamma for construction of rotation operator around axis2 
#        (list of vector components).
#        """
#        self.alpha = alpha
#        self.beta = beta
#        self.gamma = gamma
#        self.delta = delta
#        self.axis1 = axis1
#        self.axis2 = axis2
#        
#    def make(self): 
#        """
#        Output: A single qubit gate as a composition of the pauli gates
#        """
#        return (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
#               self.beta)*self.R(self.axis2, self.gamma)*self.R(self.axis1, 
#                                self.delta)
