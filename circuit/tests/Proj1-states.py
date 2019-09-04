# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 08:59:37 2019

@author: Eesh Gupta
"""

from Qubit import Qubit
from Register import register
import math

def measCatState(n, hits): 
    """
    Input: int n for number of qubits. int hits for number of measurements 
    to be performed on multiple copies of cat state
    Output: Shows measurement outputs for cat state
    """
    first_state=''
    last_state=''
    for i in range(n):
        first_state+='0'
        last_state+='1'
    print(first_state)
    print(last_state)
    
    reg=register(n)
    reg.state_vector[first_state]=1/math.sqrt(2)
    reg.state_vector[last_state]=1/math.sqrt(2)
    return reg.measure(hits = hits)

def superpositionState(n, hits): 
    """
    Input: int n for number of qubits. int hits for number of measurements 
    to be performed on multiple copies of superposition state
    Output: Shows measurement outputs for superposition state
    """
    reg=register(n)
    for key in reg.state_vector.keys():
        reg.state_vector[key] = 1/math.sqrt(2**n)
    return reg.measure(hits = hits)

    