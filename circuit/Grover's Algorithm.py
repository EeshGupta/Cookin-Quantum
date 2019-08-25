# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:01:31 2019

@author: Eesh Gupta
"""
from Register import register
import numpy as np
from QuantumCircuit import QuantumCircuit
from matplotlib import pyplot
import math

class GroverAlgo(QuantumCircuit): 
    
    def __init__(self, n, iter, needle_state):
        """
        Input: number of qubits, number of iterations and state label of answer
        """
        QuantumCircuit.__init__(self, n)
        self.iter = iter
        self.needle_state = needle_state
        self.prob_amp = []                             #For visualization
    
    @property
    def oracle(self): 
        """
        Output: Oracle operator
        """
        oracle = np.zeros((2**self.n, 2**self.n))
        
        #create Identity matrix
        for i in range(2**self.n): 
            oracle[i, i] = 1.0
        #flip needle state
        oracle[self.register.invBinDec(self.needle_state), 
               self.register.invBinDec(self.needle_state) ] = -1.0
        #Give it out
        return oracle
    
    @property
    def jOperator(self): 
        """
        Output: J operator
        """
        #Building J
        J_op = np.zeros((2**self.n, 2**self.n))
        
        #create Identity matrix
        for i in range(2**self.n): 
            J_op[i, i] = 1.0
        #flip first state
        J_op[0, 0] = -1.0
        return J_op
    
    def diffusionOp(self): 
        """
        Output: Diffusion Operator applied on stateVector
        """
        #Diffusion Subroutine
        for i in range(self.n): 
            self.applySingleQubitGate('hadamard', i)
        #print(self.stateVector)
        self.register.stateVector = self.jOperator.dot(self.register.stateVector)
        #print(self.stateVector)
        for i in range(self.n): 
            self.applySingleQubitGate('hadamard', i)
            
    def groverSubroutine(self): 
        """
        Ouput: Transformed statevector after running Grover's subroutine of 
        repeated (if iter>1) operations of oracle and diffusion operator.
        """
        for i in range(self.iter): 
            #oracle
            self.register.stateVector = self.oracle.dot(self.register.stateVector)
            #print(self.stateVector)
            #diffusion operator
            self.diffusionOp()
            self.prob_amp.append(self.register.state_vector[self.needle_state])
            
    
    def calcNeedle(self):
        """
        Output: Measurement result after implementation of Grover's algo
        """
        for i in range(self.n): 
            self.applySingleQubitGate('hadamard', i)
        #print(self.stateVector)
        self.groverSubroutine()
        print(self.register.stateVector)
        return self.measure(5)
    
    def visualization(self): 
        """
        Output: A plot of prob of needle vs iter
        """
        iterations = []
        prob = []
        
        #x axis
        for i in range(self.iter):
            iterations.append(i+1)
        #y axis
        for i in self.prob_amp: 
            prob.append(abs(i)**2)
       # print(iterations)
        #print(prob)

        #making plot
        grover_plot = pyplot
        grover_plot.plot(iterations, prob, )
        grover_plot.axis([0,self.iter,0,1])
        return grover_plot.show
        
            
            
            
#c=GroverAlgo(10, , '0000000001')
#b=c.calcNeedle()
#a= c.visualization()
#print(str((math.pi/4)*(math.sqrt(8))))

        
        