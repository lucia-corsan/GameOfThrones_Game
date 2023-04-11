# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:24:28 2020

@author: lucia
"""
import random 
class Battle:
    
    def __init__(self, location):
        self.__location = {1: "", 2: "", 3: ""}
#       self.__winner = "Winner:"
#       self.__batallion = "Batallion:"
#       self.__strength = "Strength:"
#       self.__leader = "Leader:"
#       self.__defeated = "Defeated:"
        self.__turn =  1

    #@property:
    #    def sumTurn (self):
    #        return self.__turn
        
         
    def randomBat (self, maplocation, allBatallions):
        #this method will choose a random batallion from the location selected by the user
       
        loc1 = maplocation.getLocation(allBatallions)
        #this returns the list of batallions in the selected location 
        
        randombatallion = loc1[random.randint(0, len(loc1))]
        return randombatallion
    
    #when the method finishes executing, the local variable "dies" 
    #allBatallions is the index with the game location; loc1 is the list that corresponds to that index
    
    def fight(self, maplocation, allBatallions, targaryenBat):
        randBata = self.randomBat(maplocation, allBatallions)
        #we call the whole randomBat method to be executed inside this one.
        westSoldier = randBata[random.randint(0, len(randBata))]
        targaSoldier = targaryenBat[random.randint(0, len(targaryenBat))]
        
        if westSoldier.getStrength < targaSoldier.getStrength:
           westSoldier.__strength = 0
           targaSoldier.__strength -= westSoldier.__strength/3 
           self.show(targaSoldier.getName, westSoldier.getName,allBatallions)
           self.__turn += 1
            
        else:
           westSoldier.__strength -= targaSoldier.__strength/3 
           targaSoldier.__strength = 0   
           self.show(westSoldier.getName, targaSoldier.getName,allBatallions)
           self.__turn += 1
            
  
    
    def show(self, winner, loser, location):
        
        text = "Turn" + str(self.__turn) + ':'
        text += "Battle location: " +  self.__location[location]
        text += "Winner: "  #PENDIENTE
        text += "Batallion: "
        text += "Strength: "
        text += "Leader: "
        #keep concatenating strings