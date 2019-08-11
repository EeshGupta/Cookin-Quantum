# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:58:27 2019

@author: Eesh Gupta
"""
class Qubit(object):
    def __init__(self, i, a=1, b=0):
        """
        Qubit has 2 complex amplitudes for 2 basis states, 0 and 1
        Initialized at basis state 0.
        Checks normalization condition for qubit basis state amplitudes.
        """
        self._i = i
        self._a = a
        self._b = b
        
    
    def _normalize(a, b): 
        if (a**2 +b**2) !=1: 
            raise ValueError("Amplitude values must be normalized!")
        
    @property
    def a(self): 
        return self._a
    
    @a.setter
    def a(self, value): 
        self._normalize(a = value, b = self._b)
        self._a=value
        
    @property
    def b(self): 
        return self._b
    
    @b.setter
    def b(self, value): 
        self._normalize(a = self._a, b = value)
        self._b=value