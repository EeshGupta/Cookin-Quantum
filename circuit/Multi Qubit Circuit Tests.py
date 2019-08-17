# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:08:54 2019

@author: Eesh Gupta
"""
from QuantumCircuit import QuantumCircuit
import math

def circuit1(): 
    """
    Input: A single hadamard gate on the second qubit and then 2 controls 3
    Output: measurement result (vary between 011 and 000)
    """
    circ =QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 1)
    circ.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    print(circ.register.stateVector)
    return circ.measure(2)

def circuit2(): 
    """
    Input: Second qubits acted upon by a hadamard gate and second qubit 
    controls 1  and 2 qubit
    Output: measurement result (should vary between 000 and 111)
    """
    circ =QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 1)
    circ.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    circ.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [0])
    return circ.measure(2)

def circuit3(): 
    """
    Input: Acting Hadamard gate twice on second qubit
    Output: measurement result
    """
    circ =QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 1)
    circ.applySingleQubitGate('hadamard', 1)
    return circ.measure(1)

def circuit4(): 
    """
    Input: Acting Hadamard gate twice on third qubit with a CNOT (second 
    controlling third)
    in the middle.
    Output: measurement result (vary between 000, 010, 001, 011)
    """
    circ =QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 1)
    circ.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    circ.applySingleQubitGate('hadamard', 1)
    return circ.measure(4)
