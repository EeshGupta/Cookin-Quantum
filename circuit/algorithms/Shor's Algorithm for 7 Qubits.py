# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:05:14 2019

@author: Eesh Gupta
"""

from QuantumCircuits import QuantumCircuit

class ShorAlgo(QuantumCircuit): 
    def __init__(self): 
        """
        NM
        """
    def Shor7(self, C, a): 
        """
        Input: Number to factor C and int a
        Output: Shor's result?!?
        """
        x = QuantumCircuit(3)
        x.gates.Hadamard(0)
        x.gates.Hadamard(1)
        x.gates.Hadamard(2)
        
        f = QuantumCircuit(4)
        circ = x + f
        print(circ.stateVector)
        #controls
        for i in range(3):
            circ.gates.controlShor7(control_index = i, C = C, a = a)
        #IQFT
        circ.gates.Hadamard(5)
        circ.gates.
        
        