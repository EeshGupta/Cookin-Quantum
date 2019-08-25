# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:53:18 2019

@author: Eesh Gupta
"""
import numpy as np
import math 

class gateMaker(object): 
    """Methods for other gate making subclasses"""
    def __init__(self): 
        """Nothing really"""
        
    @property
    def X(self): 
        """
        Output: Pauli X gate for a single qubit
        """
        return np.array([[0, 1], [1, 0]])
    
    @property
    def Y(self): 
        """
        Output: Pauli Y gate for a single qubit
        """
        return np.array([[0, -complex(0,1)], [complex(0,1), 0]])
    
    @property
    def Z(self): 
        """
        Output: Pauli Z gate for a single qubit
        """
        return np.array([[1, 0], [0, -1]])
    
    @property
    def I(self): 
        """
        Output: Identity gate for a single qubit
        """
        return np.array([[1, 0], [0, 1]])
    
    @property    
    def H(self): 
        """
        Output: Array repr of Hadamard operator.
        """
        return np.array([[1/math.sqrt(2), 1/math.sqrt(2)], [1/math.sqrt(2), 
                          -1/math.sqrt(2)]])
    
    @property
    def PS(self, phase): 
        """
        Output: Array repr of phase shift operator.
        """
        return np.array([[1, 0], [0, math.e**(complex(0,1)*phase)]])
    
    @property
    def CX(self):
        """
        Output: Control not gate for 2 qubits
        """
        
    
    def R(self, axis_vector, angle):
        """
        Input: Axis components in list form and angle in radians
        Output: A rotation operator
        """
        axis = (axis_vector[0]*self.X) + (axis_vector[1]*self.Y) + (axis_vector[2]*self.Z)
        
        return (math.cos(angle/2)*self.I) - complex(0,1)*(math.sin(angle/2))*(axis)
    
    def SingletoMultiQubitGateConverter(self, gate, target_qubit_index, qubits):
        """
        Input: A gate attribute, int qubit index the gate will be applied to, 
        int number of qubits.
        Output: A multi qubit gate that just messes around with asingle qubit and leaves
        the other qubits alone.
        """
        gate_opr = np.array([])                    
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

        return gate_opr