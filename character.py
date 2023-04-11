# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:52:27 2020

@author: lucia
"""

class Character:
    
    def __init__(self, category, strength, name = None, fixed_bonus = 0, var_bonus = 0):
        self.__category = category # stores the kind of character (human, archer, etc)
        self.__name = name # stores the name if the caracter has one
        self.__fixed_bonus = fixed_bonus # stores the strength to be increased in the batallion(for queen Daenerys)
        self.__var_bonus = var_bonus # stores the % of self strength to be increased in the batallion (for generals)
        self.__strength = strength # up to here the profile of the character is created
    
    @property
    def category(self):
        return self.__category # category getter - used to identify special abilities/battles
    @property
    def name(self):
        return self.__name # name getter - used to ________________________ 
    @property
    def bonus(self): # bonus getter - used to __________________________________
        return self.__fixed_bonus + self.__var_bonus*self.__strength
    @property
    def strength(self): # strength getter - used to _______________________________
        return self.__strength
