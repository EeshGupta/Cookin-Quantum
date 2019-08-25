# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:56:09 2019

@author: Eesh Gupta
"""

import numpy as np

class control(object): 
    def __init__(self, qubits, basis_states, stateVector): 
        """
        Input: int qubits, list of basis states, list of probability 
        amplitude values for those basis states
        """
        self.qubits = qubits
        self.basis_states = basis_states
        self.stateVector = stateVector
    
    def CNOT(self, control_indices, target_ind): 
        """
        Input: a list of indices of control qubits, a list of indices of target
        qubits
        Output: Statevector transformed by CNOT gate
        """
        gate = np.zeros((2**self.qubits, 2**self.qubits))
        imp_states = []
        
        #create Identity matrix
        for i in range(2**self.qubits): 
            gate[i, i] = 1.0
        #identify key state labels
        for state in self.basis_states: 
            check_state = True
            #check if all controls are set to 1
            for ind in control_indices: 
                if state[ind] == '0': 
                    check_state = False    #redundancy issues here
            if check_state: 
                imp_states.append(state)
        #pair assignment
        for control in imp_states: 
            target = control
            for ind in target_ind:
                if target[ind] == '1':
                    target = target[:ind] + '0' + target[ind + 1:]
                elif target[ind] == '0':
                    target = target[:ind] + '1' + target[ind + 1:]
                    
            #erasing the prev value in gate
            gate[self.invBinDec(control), self.invBinDec(control)] = 0.0
            #inserting the unit at a different spot
            gate[self.invBinDec(control), self.invBinDec(target)] = 1.0
        
        #applying the gate on statevector
        return gate
    

                    
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
