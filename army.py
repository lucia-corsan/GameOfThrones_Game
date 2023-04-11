# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 22:44:58 2020

@author: lucia
"""

class Army:
    
    def __init__(self):
        self.__army = [] # initialization just creates an empty list  

    def add(self, *Batallions): # this method adds battalions to the army
        for i in Batallions:
            self.__army.append(i)
    def remove(self, *Batallions): # and this one deletes them once they are dead
        for i in Batallions:
            self.__batallions.remove(i)
    
    @property
    def readArmy(self):
        return self.__army # used to read inside the army list
    
    @property
    def length(self):
        return len(self.__army) # used to get the number of batallions in the army, and iterate a variable through the indeces
       
            