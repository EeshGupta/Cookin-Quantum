# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:31:19 2019

@author: Eesh Gupta
"""

#Euclid's Algo for gcd
def EuclidGCD(a, b): 
    """
    Input: int a and b such that a>=b
    Output: Gcd of a and b
    """
    if a%b == 0: 
        return b 
    elif a%b == 1: 
        return 1
    else: 
        return EuclidGCD(b, a%b)
    
#Euclid 's algo forfinding modular inverse
            
def ForEuclidGCD(a, b, forward_dict): 
    """
    Input: int a and b such that a>=b
    Output: Gcd of a and b unless its 1; otherwise dict
    """
    forward_dict[a] = [b, a//b, a%b]
    
    if a%b == 0: 
        return b 
    elif a%b == 1: 
        return forward_dict
    else: 
        return EuclidGCD(b, a%b)

def DictConverter(forward_dict): 
    """
    Input: dict forward_dict from forward Euclid Algo
    Output: dict backward_dict for backward Euclid Algo
    """
    backward_dict = {}
    keys = []
    
    for key in forward_dict.keys(): 
        keys.append(key)
    keys.reverse()
    for key in keys: 
        backward_dict[forward_dict[key][2]] = [key, 1, forward_dict[key][0], 
                      forward_dict[key][1]]
    return backward_dict

def DictTranslator(backward_dict): 
    """
    Input: backward_dict
    Function: Perform Euclid's backward algo
    Output: A list 
    """
    listy = []
    keys = []
    
    for key in backward_dict.keys(): 
        keys.append(key)
    keys.remove(1)
    
    listy = [[backward_dict[1][0], backward_dict[1][1]], 
             [backward_dict[1][2], backward_dict[1][3]]]
    listy.reverse()
    for key in keys: 
        if key == listy[1][1]: 
            c = listy[0][1]
            
            listy[0][0] = backward_dict[key][0]
            listy[0][1] = c*(backward_dict[key][1])
            if listy[1][0] == backward_dict[key][2]: 
                listy[1][1] == listy[1][1] + c*backward_dict[key][3]
            listy.reverse()
        else: 
            raise ValueError("Something in wrong")
    return listy

def BackwardAlgo(backward_dict, num , modulo): 
    """
    Input: dict backward_dict, int num and modulo
    Output: the modular inverse
    """
    listy = DictTranslator(backward_dict = backward_dict)
    
    if listy[0] == modulo and listy[2] == num: 
        return listy[3]
    else: 
        raise ValueError("Something in wrong")

def main(num, modulo): 
    """
    Input: int num and modulo
    Output: modular inverse
    """
    forward_dict = {}
    
    forward_result = ForEuclidGCD(num, modulo, forward_dict = forward_dict)
    if type(forward_result) == dict: 
        return BackwardAlgo(backward_dict = DictConverter(forward_dict = forward_dict),
                            num = num , modulo = modulo)
    elif type(forward_result) == int: 
        msg = "No inverse modulo exists"
        return msg
    else: 
        raise ValueError("Something went wrong")
    
    