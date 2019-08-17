# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 11:15:33 2019

@author: Eesh Gupta
"""

from QuantumCircuit import QuantumCircuit
import math

def circuit1(): 
    """
    Input: A single hadamard gate on the second qubit
    Output: measurement result
    """
    circ = QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 1)
    print(circ.register.stateVector)
    return circ.measure(1)

def circuit2(): 
    """
    Input: All qubits acted upon by a hadamard gate
    Output: measurement result
    """
    circ = QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 0)
    circ.applySingleQubitGate('hadamard', 1)
    circ.applySingleQubitGate('hadamard', 2)
    return circ.measure(1)

def circuit3(): 
    """
    Input: Acting Hadamard gate twice on third qubit
    Output: measurement result
    """
    circ = QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 2)
    circ.applySingleQubitGate('hadamard', 2)
    return circ.measure(1)

def circuit4(): 
    """
    Input: Acting Hadamard gate twice on third qubit with a phase shift gate
    in the middle.
    Output: measurement result
    """
    circ = QuantumCircuit(3)
    circ.applySingleQubitGate('hadamard', 2)
    circ.applySingleQubitGate('phase shift', 2, math.pi)
    circ.applySingleQubitGate('hadamard', 2)
    return circ.measure(1)