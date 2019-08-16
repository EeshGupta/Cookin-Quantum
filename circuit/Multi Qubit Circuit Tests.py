# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:08:54 2019

@author: Eesh Gupta
"""
from Register import register
import math

def circuit1(): 
    """
    Input: A single hadamard gate on the second qubit and then 2 controls 3
    Output: measurement result (vary between 011 and 000)
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 1)
    reg.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    return reg.measure(2)

def circuit2(): 
    """
    Input: Second qubits acted upon by a hadamard gate and second qubit 
    controls 1  and 2 qubit
    Output: measurement result (should vary between 000 and 111)
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 1)
    reg.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    reg.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [0])
    return reg.measure(2)

def circuit3(): 
    """
    Input: Acting Hadamard gate twice on second qubit
    Output: measurement result
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 1)
    reg.applySingleQubitGate('hadamard', 1)
    print(reg.stateVector)
    return reg.measure(1)

def circuit4(): 
    """
    Input: Acting Hadamard gate twice on third qubit with a CNOT (second 
    controlling third)
    in the middle.
    Output: measurement result (vary between 000, 010, 001, 011)
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 1)
    reg.applyMultiQubitGate('CNOT', control_ind = [1], target_ind = [2])
    reg.applySingleQubitGate('hadamard', 1)
    return reg.measure(4)
