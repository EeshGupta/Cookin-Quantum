# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:56:40 2019

@author: Eesh Gupta
"""

import numpy as np

class groverGates(object): 
    def __init__(self): 
        """
        Organization is cool
        """

    def oracle(self, n, needle_state): 
        """
        Output: Oracle operator
        """
        oracle = np.zeros((2**n, 2**n))
        
        #create Identity matrix
        for i in range(2**n): 
            oracle[i, i] = 1.0
        #flip needle state
        oracle[self.invBinDec(needle_state), 
               self.invBinDec(needle_state) ] = -1.0
        #Give it out
        return oracle

    def jOperator(self, n): 
        """
        Output: J operator
        """
        #Building J
        J_op = np.zeros((2**n, 2**n))
        
        #create Identity matrix
        for i in range(2**n): 
            J_op[i, i] = 1.0
        #flip first state
        J_op[0, 0] = -1.0
        return J_op

    def invBinDec(self, Binary):
        """
        Input: Binary (a string)
        Output: Decimal repr (an int)
        """
        dec=0
        length= len(Binary)
        for i in range(length):
            if Binary[length-i-1] == '1':
                dec += 2**(i)
        return dec