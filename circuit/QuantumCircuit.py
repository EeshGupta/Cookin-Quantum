# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:24:46 2019

@author: Eesh Gupta
"""
from Register import register
from GateBuilder import gates
import numpy as np
import math

class QuantumCircuit(object): 
    """Main Class of the Quantum Circuit Simulator"""
    
    def __init__(self, n):
        """
        n: Number of Qubits
        """
        self.n = n 
        self.register = register(self.n)
        
#        #Setting StateVector
#        if stateVector != None: 
#            self.stateVector = stateVector
#        else: 
#            self.register.stateVector = stateVector
#            self.stateVector = self.register.stateVector
            
        self.gates = gates(self.n, self.register.state_vector)

    def __add__(self, other):
        """
        Input: 2 Quantum Circuits
        Output: A new circuit as a combo of the 2 inputted.
        """        
        new_circ = QuantumCircuit(n = self.n + other.n)
        new_circ.stateVector = np.kron(self.stateVector, other.stateVector)
        return new_circ

    def measure(self, hits): 
        """
        Input: int hits= Number of times the measurements must be performed
        Output: A list of resultant qubits with a length of # of hits
        """
        prob=[]
        keys=[]
        result=[]
        
        #EEE statevectors
        self.stateVector = self.gates.stateVector
        self.register.stateVector = self.gates.stateVector
        #List of probabilities
        state_vector= self.stateVector
        state_vector=state_vector.reshape((2**self.n))
        for val in state_vector:
            prob.append(abs(val)**2)
        #List of states
        for key in self.register.state_vector.keys(): 
            keys.append(key)
        #List of indixes of states
        indices = list(range(0, len(self.register.state_vector.keys())))
        #Measurement
        draw = np.random.choice(a=indices, size = hits, p=prob)
        for i in range(len(draw)): 
            result.append(keys[draw[i]])
        return result
    
    #getter for self.state_vector
    @property    
    def stateVector(self): 
        """
        Output: StateVector
        """
        #Updating stateVector in register from gates
        self.register.stateVector = self.gates.stateVector
        return self.register.stateVector
    
    @stateVector.setter
    def stateVector(self, stateVector): 
        """
        Input: An array of values for different basis states
        Function: Uses the setter of register's statevector
        """
        self.register.stateVector = stateVector
        #self.stateVector = self.register.stateVector
    
###Tests###
circ =QuantumCircuit(2)
circ.gates.Hadamard(1)
g= circ.gates.stateVector
r= circ.register.stateVector
#circ.gates.CU1(0,1,math.pi, math.pi, math.pi/2, math.pi)
g= circ.gates.stateVector

circ1=QuantumCircuit(2)
circ2 = circ1 + circ

