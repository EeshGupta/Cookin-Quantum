# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:15:33 2019

@author: Eesh Gupta
"""

from Register import register
import math

def circuit1(): 
    """
    Input: A single hadamard gate on the second qubit
    Output: measurement result
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 1)
    print(reg.stateVector)
    return reg.measure(1)

def circuit2(): 
    """
    Input: All qubits acted upon by a hadamard gate
    Output: measurement result
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 0)
    reg.applySingleQubitGate('hadamard', 1)
    reg.applySingleQubitGate('hadamard', 2)
    return reg.measure(1)

def circuit3(): 
    """
    Input: Acting Hadamard gate twice on third qubit
    Output: measurement result
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 2)
    reg.applySingleQubitGate('hadamard', 2)
    return reg.measure(1)

def circuit4(): 
    """
    Input: Acting Hadamard gate twice on third qubit with a phase shift gate
    in the middle.
    Output: measurement result
    """
    reg =register(3)
    reg.applySingleQubitGate('hadamard', 2)
    reg.applySingleQubitGate('phase shift', 2, math.pi)
    reg.applySingleQubitGate('hadamard', 2)
    return reg.measure(1)