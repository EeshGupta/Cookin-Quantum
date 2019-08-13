# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:50:43 2019

@author: Eesh Gupta
"""

from circuit.Register import register
import numpy as np

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
        return np.array([[1, 1], [1, -1]])
    
    def buildApplyGate(self, gate, target_qubit_index, qubits, state_vector):
        """
        Input: A gate attribute, int qubit index the gate will be applied to, 
        int number of qubits, an array to be transformed. 
        Output: Transformed state Vector
        """
        gate_opr = np.array()
        
        #repeated tensor products to build the gate matrix
        for i in range(0, target_qubit_index):
            if i == 0: 
                gate_opr = self.I
            else: 
                gate_opr = np.tensordot(gate_opr, self.I)
        if target_qubit_index == 0: 
            gate_opr = self.gate
        else:
            gate_opr = np.tensordot(gate_opr, self.gate)
        for i in range(target_qubit_index + 1, qubits): 
            gate_opr = np.tensordot(gate_opr, self.I)
        
        #applying the gate on register
        return gate_opr.dot(state_vector)
            
            