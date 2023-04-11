# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:33:40 2020

@author: lucia
"""

class Map:
    
    def __init__(self): # Kept the numbers here for simplicity. 
        self.__map = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]} 
      # 1- King's landing, 2- Winterfell, 3- The Wall, 4- Storm's end, 5- Riverrun, 6- Casterlyrock, 7- Sunspear
    
    def addBatallion(self, Batallion, location): # adds battalions to location
        self.__map[location].append(Batallion)
        
    def delBatallion(self, Batallion, location): # deletes batallions
        self.__map[location].remove(Batallion)
    
    def names(): # "Translates" the numbers to the real names (for the display of the results)
        return {1:"King's landing", 2:"Winterfell", 3:"The Wall", 4:"Storm's end", 5:"Riverrun", 6:"Casterlyrock", 7:"Sunspear"}
        