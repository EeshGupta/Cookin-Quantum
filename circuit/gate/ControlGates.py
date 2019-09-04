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
            gate[self.BinToDec(Binary = control), self.BinToDec(Binary = control)] = 0.0
            #inserting the unit at a different spot
            gate[self.BinToDec(control), self.BinToDec(target)] = 1.0
        
        #applying the gate on statevector
        return gate

    def controlShor7(self, control_index, a, C): 
        """
        Input: int control_index and int a
        Output: Make control f gates for Shor's algorithm
        """
        new_control_ind = 2 - control_index
        gate = np.zeros((128, 128))
        
        for i in range(128):
            bin_i = self.bin_spec(i)
            if bin_i[new_control_ind] == 1 and self.BinToDec(bin_i[3:]) < C:
                new_index = self.bin_spec(((a**(2**control_index))*
                                           self.BinToDec(bin_i[3:]))%C)
                print(new_index)    #debug
                new_index = bin_i[:3] + new_index
                gate[self.BinToDec(new_index), i] = 1.0   
            else: 
                gate[i,i] = 1.0
        return gate
    
     def CNOTPHASE(self, control_index, target_index, phase): 
        """
        Input: control index, target index and phase
        Output: Statevector transformed by CNOTPHASE gate
        """
        gate = np.zeros((2**self.qubits, 2**self.qubits))
        imp_states = []
        
        #create Identity matrix
        for i in range(2**self.qubits): 
            gate[i, i] = 1.0
        #identify key state labels
        for state in self.basis_states: 
            if state[control_index] == '1' and state[target_index] == '1': 
                gate[self.BinToDec[state], self.BinToDec[state]] == math.e**(complex(0,0)*phase)
        
        #applying the gate on statevector
        return gate
    
    def bin_spec(self, n): 
        """
        Input: int n in assumed decimal representation
        Output: A 7 digit binary representation of n.
        """
        a=self.DecToBin(n)
        #print(a)
        while len(a) != 7:
            a =  '0' + a 
        return a
    
    def DecToBin(self, n):
        """
        Input: int n in assumed decimal representation
        Output: Inverted Binary representation of input n
        """
        if n==0: 
            return '0'
        elif n==1: 
            return '1'
        else: 
            return   self.DecToBin(n//2) + str(n%2)                       
    
    def BinToDec(self, Binary):
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
#
test = control(3, ['000','001','010', '011', '100','101','110', '111'], [1,0,0,0,])
a= test.CNOT([0],[2])






