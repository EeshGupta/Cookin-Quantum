# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:50:43 2019

@author: Eesh Gupta
"""

import numpy as np
import math

class gates(object): 
    def __init__(self): 
        """
        nothing
        """
   
    @property
    def I(self):
        """
        Output: Array repr of Identity operator.
        """
        return np.array([[1, 0], [0, 1]])
      
    @property    
    def H(self): 
        """
        Output: Array repr of Hadamard operator.
        """
        return np.array([[1/math.sqrt(2), 1/math.sqrt(2)], [1/math.sqrt(2), 
                          -1/math.sqrt(2)]])
    
    def PS(self, phase): 
        """
        Output: Array repr of phase shift operator.
        """
        return np.array([[1, 0], [0, math.e**((0+j)*phase)]])
    
    def gateConverter(self, gate, phase): 
        """
        Input: some string
        Output: corresponding operator/gate
        """
        if type(gate)==str:
            
            if gate == 'identity':
                return self.I
            elif gate == 'hadamard': 
                return self.H
            elif gate == 'phase shift':
                return self.PS(phase)
        else: 
            raise ValueError("input arg gate should be a string")
    
    def buildApplyGate(self, gate, target_qubit_index, qubits, state_vector, 
                       phase):
        """
        Input: A gate attribute, int qubit index the gate will be applied to, 
        int number of qubits, an array to be transformed. A phase arg for 
        phase shift gate only.
        Output: Transformed state Vector
        """
        gate_opr = np.array([])
        target_qubit_index = qubits - target_qubit_index - 1
        
        #Gate Conversion
        gate= self.gateConverter(gate, phase)
            
        
        #repeated tensor products to build the gate matrix
        for i in range(0, target_qubit_index):
            if i == 0: 
                gate_opr = self.I
            else: 
                gate_opr = np.kron(gate_opr, self.I)
        if target_qubit_index == 0: 
            gate_opr = gate
        else:
            gate_opr = np.kron(gate_opr, gate)
        for i in range(target_qubit_index + 1, qubits): 
            gate_opr = np.kron(gate_opr, self.I)
        
        #applying the gate on register
        return gate_opr.dot(state_vector)
            
