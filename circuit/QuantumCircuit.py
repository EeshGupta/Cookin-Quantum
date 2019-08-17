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

    def applySingleQubitGate(self, gate, target_qubit_index, phase = None): 
        """
        Input: A single qubit gate object to be applied on an int qubit index from qubit 
        list. Input phase if gate is phase shift gate.
        Output: Transformed stateVector
        """
        newGate = gates()
        self.register.stateVector = newGate.SingleQubitGate( gate = gate, 
                                                  target_qubit_index = target_qubit_index, 
                                                  qubits = self.n, 
                                                  stateVector = self.register.stateVector, 
                                                  phase = phase)

    def applyMultiQubitGate(self, gate, control_ind, target_ind): 
        """
        Assumes CNOT Gate
        Input: A multi qubit gate with control qubits specified by int in list 
        of control ind and target qubits specified by int in list target qubit. 
        Output: Transformed stateVector
        """
        basis_labels = []
        newGate = gates()
        
        #getting basis state labels
        for key in self.register.state_vector.keys(): 
            basis_labels.append(key)
        #calling gate function
        self.register.stateVector = newGate.CNOT(control_ind = control_ind, 
                                        target_ind = target_ind, 
                                        qubit_size = self.n, 
                                        basis_labels = basis_labels, 
                                        stateVector= self.register.stateVector)
    def measure(self, hits): 
        """
        Input: int hits= Number of times the measurements must be performed
        Output: A list of resultant qubits with a length of # of hits
        """
        prob=[]
        keys=[]
        result=[]
        
        #List Of Probabilities
        state_vector= self.register.stateVector
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
    
circ =QuantumCircuit(2)
circ.applySingleQubitGate('hadamard', 1)
c= circ.applyMultiQubitGate('CNOT', control_ind = [0], target_ind = [1])