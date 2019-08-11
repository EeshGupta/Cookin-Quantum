# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:58:27 2019

@author: Eesh Gupta
"""
class Qubit(object):
    def __init__(self):
        """
        Qubit has 2 complex amplitudes for 2 basis states, 0 and 1
        Initialized at basis state 0.
        Checks normalization condition for qubit basis state amplitudes.
        """
        self.a=1
        self.b=0
        if ((self.a)**2 +(self.b)**2)!= 1: 
            raise ValueError("Qubit state should be normalized. Re-assign" + 
                             "valid amplitudes to the Qubit ")
        