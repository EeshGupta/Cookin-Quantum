# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:53:07 2019

@author: Eesh Gupta
"""
import numpy as np
from Qubit import Qubit
class register: 
    def __init__(self, n): 
        """
        Input: Positive integer n to denote number of qubits
        """
        self.n=n
        self.qubits= createQubits()
        self.state_vector=createStateVector()
    def createQubits(self):  
        """
        Input: Number of qubits
        Output: A list of qubit objects
        """
        qubit_list=[]
        for i in range(self.n): 
            qubit_list.append(Qubit(i))
        return qubit_list
    
    def createStateVector(self):
        """
        Output: Create a column vector representation of the tensor product of 
        n qubits
        """
#        state_vector=np.zeros((2**self.n,1))
#        updatestatevector(state_vector)
#        return state_vector
        state_vector={}
        for i in range(2**(self.n)):
            c=bin_spec(i)
            state_vector[c]=0.0
        return updateStateVector(state_vector)
    
    def updateStateVector(self, state_vector=self.state_vector):
        """
        Output: Updates the amplitudes of basis states of combined system
        """
        for key in state_vector.keys(): 
            c=1
            for i in range(len(key)): 
                if key[i] == '0': 
                    c=c*(self.qubits(i).a)
                elif key[i]=='1':
                    c=c*(self.qubits(i).b)
            state_vector[key]=c
        
            
    def bin_spec(self, n): 
        a=dec_to_bin(n)
        while len(a) != self.n:
            a='0'+a
        return a
    
    def dec_to_bin(n): 
        if n==0: 
            return '0'
        elif n==1: 
            return '1'
        else: 
            return str(n%2) + dec_to_bin(n//2)

            
            
        

