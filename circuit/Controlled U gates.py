# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:29:39 2019

@author: Eesh Gupta
"""
import numpy as np
import math

class controlledUGate(gateMaker): 
    def __init__(self, control qubits, targestateVector, ): 
        
        
    @proprty   
    def CNOT(self):
        """
        Output: CNOT gate
        """
        return np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    
    def V(self, beta, gamma, delta, stateVector): 
        """
        Input: angle values to construct rotation opertors satisfying AXBXC 
        decomposition of a unitary operator.
        Output: Unitary matrix
        """
        Z_axis = [0, 0, 1]
        Y_axis = [0, 1, 0]
        
        A= self.R(Z_axis, beta)*self.R(Y_axis, gamma/2)
        B= self.R(Y_axis, -gamma/2)*self.R(Z_axis, -(delta +beta)/2)
        C= self.R((delta - beta)/2)
        