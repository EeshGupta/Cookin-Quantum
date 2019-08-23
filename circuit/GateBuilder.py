# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:50:43 2019

@author: Eesh Gupta
"""

import numpy as np
import math
import cmath

class gates(object): 
    
    def __init__(self): 
        """
        controls all operations of operators
        """
   
   #Single Qubit Gates 
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
    
    @property
    def PS(self, phase): 
        """
        Output: Array repr of phase shift operator.
        """
        return np.array([[1, 0], [0, math.e**(complex(0,1)*phase)]])
    
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
    
    def SingleQubitGate(self, gate, target_qubit_index, qubits, stateVector, 
                       phase):
        """
        Input: A gate attribute, int qubit index the gate will be applied to, 
        int number of qubits, an array to be transformed. A phase arg for 
        phase shift gate only.
        Output: Transformed state Vector
        """
        gate_opr = np.array([])
        #target_qubit_index = qubits - target_qubit_index - 1
        
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
        
        #return gate_opr
        #applying the gate on register
        return self.applyGate(gate_opr, stateVector)
    
    #Multiple Qubit Gates
    def CNOT(self, control_ind, target_ind, qubit_size, basis_labels, 
             stateVector): 
        """
        Input: a list of indices of control qubits, a list of indices of target
        qubits, number of qubits, a list of labels of basis states of 
        system(register), array stateVector
        Output: Statevector transformed by CNOT gate
        """
        gate = np.zeros((2**qubit_size, 2**qubit_size))
        imp_states = []
        
        #create Identity matrix
        for i in range(2**qubit_size): 
            gate[i, i] = 1.0
        #identify key state labels
        for state in basis_labels: 
            check_state = True
            #check if all controls are set to 1
            for ind in control_ind: 
                if state[ind] == '0': 
                    check_state = False    #redundancy issues here
            if check_state: 
                imp_states.append(state)
        #print(imp_states)
        #pair assignment
        for control in imp_states: 
            target = control
            #print(control)
            for ind in target_ind:
                if target[ind] == '1':
                    target = target[:ind] + '0' + target[ind + 1:]
                elif target[ind] == '0':
                    target = target[:ind] + '1' + target[ind + 1:]
            #print(target)
                    
            #erasing the prev value in gate
            gate[self.invBinDec(control), self.invBinDec(control)] = 0.0
            #inserting the unit at a different spot
            gate[self.invBinDec(control), self.invBinDec(target)] = 1.0
        
        #applying the gate on register
        #return gate debug
        return self.applyGate(gate, stateVector)
                    
    #helper method for CNOT
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
    
    def applyGate(self, gate, stateVector): 
        """
        Input: A single of multiple qubit gate
        Ouput: Transformed State Vector
        """
        return gate.dot(stateVector)
#sSOme Tests
c= gates()
a=c.SingleQubitGate('hadamard', 1, 2, [1,0,0,0], phase = None)
        
            
