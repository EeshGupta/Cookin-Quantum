# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:50:43 2019

@author: Eesh Gupta
"""

import numpy as np
import math
import cmath
from GateMaker import gateMaker
from GroverGates import groverGates
from ControlGates import control

class gates(gateMaker): 
    
    def __init__(self, qubits, state_vector): 
        """
        controls all operations of operators
        Input: int number of qubits, state_vector dict
        """ 
        self.qubits = qubits
        self.basis_states = []
        self.stateVector = []
        
        for key in state_vector.keys(): 
            self.basis_states.append(key)
        for amp in state_vector.values(): 
            self.stateVector.append(amp)
            
        self.control = control(self.qubits, self.basis_states, self.stateVector)
        
#####################        Single Qubit Gates          ######################
    def Hadamard(self, target_qubit_index):
        """
        Input:  int target_qubit_index
        Output: Applied Hadamard on target Qubit and transformed Statevector
        """
        gate = self.SingletoMultiQubitGateConverter(self.H, target_qubit_index = target_qubit_index,
                                                    qubits = self.qubits)
        return self.applyGate(gate)

    def PhaseShift(self, target_qubit_index, phase):
        """
        Input:  int target_qubit_index
        Output: Applied Hadamard on target Qubit and transformed Statevector
        """
        gate = self.SingletoMultiQubitGateConverter(gate = self.PS(phase = phase),
                                                     target_qubit_index = target_qubit_index,
                                                    qubits = self.qubits)
        return self.applyGate(gate)
    
    
    def singleQubitGateMaker1Axis(self, alpha, theta, axis1): 
        """
        Input: Angle alpha for phase, angle theta for construction of rotation
        operator around axis1 (list of vector components).

        Output: A single qubit gate as a composition of the pauli rotation
        operators
        
        *Decomposition of unitary gate into 1 rotation operator 
        """
        gate = (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
               self.theta)
        return self.applyGate(gate)
    
    def singleQubitGateMaker2Axes(self, alpha, beta, gamma, delta, axis1, axis2):
        """ 
        *Decomposition of unitary gate into 2 rotaion operators
        (eg. XY and ZY)
    
        Input: Angle alpha for phase, angles beta and delta for contruction of 
        respective rotation operators around axis1 (list of vector components), 
        angle gamma for construction of rotation operator around axis2 
        (list of vector components).
    
        Output: A single qubit gate as a composition of the pauli gates
        """
        gate = (math.e**(complex(0,1)*self.alpha))*self.R(self.axis1, 
               self.beta)*self.R(self.axis2, self.gamma)*self.R(self.axis1, 
                                self.delta)
        return self.applyGate(gate)
    
###############################################################################
    def CNOT(self, control_indices, target_ind): 
        """
        Input: a list of indices of control qubits, a list of indices of target
        qubits
        Output: Statevector transformed by CNOT gate
        """
        return self.applyGate(self.control.CNOT(control_indices, target_ind))
    
    def Toffoli(self, control1_index, control2_index, target_index): 
        """
        Input: int 2 control indices and 1 target indices
        Output: Implements the toffoli gate on circuit
        """
        return self.CNOT(control_indices = [control1_index, control2_index], 
                         target_ind = [target_index])
    
    def CU1(self, control_index, target_index, alpha, beta, gamma, delta): 
        """
        Input: int control index and int target index. angle values to construct
        rotation opertors satisfying AXBXC decomposition of a unitary operator.
        
        Output: Applies Controlled U gate and transforms stateVector
        """
        Z_axis = [0, 0, 1]
        Y_axis = [0, 1, 0]
        
        A= (math.e**(complex(0,1)*alpha))*self.R(Z_axis, beta)*self.R(Y_axis, gamma/2)
        B= self.R(Y_axis, -gamma/2)*self.R(Z_axis, -(delta +beta)/2)
        C= self.R(Z_axis, (delta - beta)/2)
        
        #Performing the operations AXBXC
        #A
        gateA = self.SingletoMultiQubitGateConverter(gate = A,
                                                     target_qubit_index = target_index,
                                                    qubits = self.qubits)
        self.applyGate(gateA)
        #X
        self.CNOT(control_indices = [control_index], target_ind = [target_index])
        #B
        gateB = self.SingletoMultiQubitGateConverter(gate = B,
                                                     target_qubit_index = target_index,
                                                    qubits = self.qubits)
        self.applyGate(gateB)
        #X
        self.CNOT([control_index], [target_index])
        #C
        gateC = self.SingletoMultiQubitGateConverter(gate = C,
                                                     target_qubit_index = target_index,
                                                    qubits = self.qubits)
        self.applyGate(gateC)
        
#    def CUN(self, n, alpha, beta, gamma, delta): 
#        """
#        Input: int n (first n qubits are control n+1 is target), angle values 
#        in radians for U gate
#        Output: Perform controlled U operation with n control qubits
#        """
#        
#        #creating a helper circuits
#        #current
#        circ1 = QuantumCircuit(self.qubits)
#        circ1.stateVector = self.stateVector
#        #WorkQubits
#        circ2 = QuantumCircuit(n - 1)
#        #Helper Circuit
#        circ3 = circ2 + circ1
#        
#        #Algorithm with toffoli gates and work qubits
#        c = n+1
#        w = 1
#        
#        circ3.gates.Toffoli(n-1, n, 0)
#        while c <= 2n-2 and w <= n-2: 
#            circ3.gates.Toffoli(c, w-1, w)
#            c+=1
#            w+=1
#            
#        circ3.gates.CU1(w, 2n - 1, alpha, beta, gamma, delta)
#        
#        while c >= n+1 and w >= 1: 
#            circ3.gates.Toffoli(c, w-1, w)
#            c-=1
#            w-=1
#        circ3.gates.Toffoli(n-1, n, 0)
#            
        

######################      Grover's Algo gate      ###########################

    def Oracle(self, needle_state): 
        """
        Applies the oracle onto stateVector
        """
        g = groverGates()
        return self.applyGate(g.oracle(n = self.qubits, needle_state = needle_state))
    
    def J(self): 
        """
        Applies the oracle onto stateVector
        """
        g = groverGates()
        return self.applyGate(g.jOperator(n = self.qubits))
    
        
###############################################################################
        
    def applyGate(self, gate): 
        """
        Input: A single of multiple qubit gate
        Ouput: Transformed State Vector
        """
        self.stateVector = gate.dot(self.stateVector)
        
#sSOme Tests
#c= gates()
#a=c.SingleQubitGate('hadamard', 1, 2, [1,0,0,0], phase = None)
        
            
