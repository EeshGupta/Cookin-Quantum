# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:53:07 2019

@author: Eesh Gupta
"""
import numpy as np
from Qubit import Qubit
import cmath
import math

class register(object): 
    """Register Class controls qubits and statevector methods"""
    def __init__(self, n): 
        """
        Input: Positive integer n to denote number of qubits
        """
        self.n = n
        self.qubits= self.createQubits()
        self.state_vector=self.createStateVector()
        self.updateStateVector()
        
    def createQubits(self):  
        """
        Input: Number of qubits
        Output: A list of qubit objects
        """
        qubit_list=[]
        for i in range(self.n): 
            qubit_list.append(Qubit(i))
        return qubit_list

    #StateVector Methods
    def createStateVector(self):
        """
        Output: Create a column vector representation of the tensor product of 
        n qubits
        """
        state_vector={}
        for i in range(2**(self.n)):
            #print(i)
            c=self.bin_spec(i)
            #print(c)
            state_vector[c]=0.0
        return state_vector
    
    def updateStateVector(self):
        """
        ***To be used only when changing amplitudes of 
        individual qubits directly***
        
        Output: Updates the amplitudes of basis states of combined system
        """
        for key in self.state_vector.keys(): 
            amp=1
            for i in range(len(key)): 
                if key[i] == '0': 
                    amp = amp*(self.qubits[i].a)
                elif key[i] == '1':
                    amp = amp*(self.qubits[i].b)
            self.state_vector[key] = amp
#        
            
    def bin_spec(self, n): 
        """
        Input: int n in assumed decimal representation
        Output: A self.n digit inverted binary representation of n.
        """
        a=self.dec_to_bin(n)
        #print(a)
        while len(a) != self.n:
            a =  '0' + a 
        return a
    
    def dec_to_bin(self, n):
        """
        Input: int n in assumed decimal representation
        Output: Inverted Binary representation of input n
        """
        if n==0: 
            return '0'
        elif n==1: 
            return '1'
        else: 
            return   self.dec_to_bin(n//2) + str(n%2)
            
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
    
    
    
#getter for self.state_vector
    @property    
    def stateVector(self): 
        """
        Output: Proper array repr of state vector array
        """
        state_vector_arr= np.array([])
        values=[]
        
        #complexify the state_vector_arr
        for i in range(2**self.n): 
            state_vector_arr = np.append(state_vector_arr, [complex(0,0)])
        state_vector_arr = state_vector_arr.reshape((2**self.n, 1))
        
        #Creating repr
        for val in self.state_vector.values():
            values.append(val)
        for i in range(2**self.n):
            state_vector_arr[i,0]=values[i]
        return state_vector_arr
    
    @stateVector.setter
    def stateVector(self, state_vector): 
        """
        Input: An array of values for different basis states
        Function: Assigns those values to respective dict keys in internal
        repr of state vector
        """
        #check for normalization condition
        value = 0 
        #print(state_vector)
        for val in state_vector: 
            value += (abs(val))**2
        
        #print(value)
        if value >=0.999 and value <=1.001: 
            #initializing keys list
            keys=[]
            for key in self.state_vector.keys(): 
                keys.append(key)
            #checking length constraint
            if len(keys) == len(state_vector):
                for i in range(len(keys)): 
                    self.state_vector[keys[i]] = state_vector[i]
            else: 
                raise ValueError("Length of stateVector must be equal to " + 
                                 str(2**self.n) + ".")
        else: 
            raise ValueError("stateVector must be normalized!")


        

            
            
        

