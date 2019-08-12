# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:58:27 2019

@author: Eesh Gupta
"""
class Qubit(object):
   
    def __init__(self, i =None, a=1, b=0):
        """
        Input: 2 complex amplitudes, a and b, for 2 basis states, 0 and 1
               int i to refer to as id. Used for identification for register.
        
        """
        self._a = a
        self._b = b
        self._id=i
        
    
    def _normalize(self, a, b): 
        """
        Input: int a and b 
        Output: Checks if amplitudes are normalized.
        """
        a=int(a)
        b=int(b)
        if (a**2 +b**2) !=1: 
            raise ValueError("Amplitude values must be normalized!")
        
    @property
    def a(self): 
        return self._a
    
    @a.setter
    def a(self, value): 
        if abs(value)<=1: 
            self._a=value
            self._b=math.sqrt(1-((abs(value))**2))
        else: 
            raise ValueError("Since Amplitude values must be normalized," + 
                             " norm of a must be less than or equal to 1")
            
    @property
    def b(self): 
        return self._b
    
    @b.setter
    def b(self, value): 
        if abs(value)<=1: 
            self._b=value
            self._a=sqrt(1-((abs(value))**2))
        else: 
            raise ValueError("Since Amplitude values must be normalized," + 
                             " norm of b must be less than or equal to 1")
