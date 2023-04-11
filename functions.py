# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:25:28 2020

@author: lucia
"""
def setupWesterosArmy():
    # SETUP OF WESTEROS ARMY ################################################################
    import random
    from map import Map
    from army import Army
    from batallion import Batallion
    from character import Character
    
    mapWesteros = Map()
    westerosArmy = Army()
    
    a, b, c = 20, 10, 5 # number of battalions of each kind (human-archer-undead)
    
    #creating the generals. they must join 5 different human battalions
    # so we extract 5 random numbers between 0 and a+b (any larger number corresponds
    # to an undead battalion) and append them there
    generalTywin = Character("general", 300, name = "Tywin", var_bonus = 0.1) 
    generalJaimie = Character("general", 250, name = "Jaimie", var_bonus = 0.1) 
    generalCersei = Character("general", 200, name = "Cersei", var_bonus = 0.1) 
    generalTyrion = Character("general", 150, name = "Tyrion", var_bonus = 0.1) 
    generalStannis = Character("general", 300, name = "Stannis", var_bonus = 0.1) 
    generals = []
    generals.append(generalTywin)
    generals.append(generalJaimie)
    generals.append(generalCersei)
    generals.append(generalTyrion)
    generals.append(generalStannis)
    
    aux = []
    while len(aux) < 5:
        aux2 = random.randint(0, a+b) # 5 different random numbers we will use later
        if aux2 not in aux:
            aux.append(aux2)
    
    
    for i in range(a): # adding a batallions of 100 human soldiers
        W_human = Batallion()
        if i in aux:
            W_human.addCharacter(generals[aux.index(i)]) # appending generals at (previously) randomly chosen batallions
        for i in range(100):
            human_soldier = Character("human soldier", random.randint(10, 50))
            W_human.addCharacter(human_soldier)# appending the humans to the batallion
        westerosArmy.add(W_human)# adding batallion to army
    
    ### we have not created a function for this part because we are appending the generals/undead king on the way
    
    for i in range(b): # adding b batallions of 100 archers
        W_archer = Batallion()
        if i+a in aux:
            W_human.addCharacter(generals[aux.index(i+a)]) # appending generals at (previously) randomly chosen batallions
        for i in range(100):
            human_archer = Character("archer", random.randint(10, 20))
            W_archer.addCharacter(human_archer)# appending the archers to the batallion
        westerosArmy.add(W_archer)# adding batallion to armyv
    
    aux3 = random.randint(0,4)
    undeadKing = Character("undead king", 500) # creating the undead king
    for i in range(c): # adding c batallions of 100 undead soldiers
        W_undeadSoldier = Batallion()
        if i == aux3:
            W_undeadSoldier.addCharacter(undeadKing) # randomly appending the undead king to one of the battalions
        for i in range(100):
            undeadSoldier = Character("undead soldier", random.randint(30, 60)) # appending the undead soldiers to the batallion
            W_undeadSoldier.addCharacter(undeadSoldier)
        westerosArmy.add(W_undeadSoldier)# adding batallion to army
    
    for i in range(westerosArmy.length):
        mapWesteros.addBatallion(westerosArmy.readArmy[i], random.randint(1,7))
    
    return mapWesteros, westerosArmy




# MENU
def menuDisplay(turn, step = 1, testing_DeveloperTool = False, firstAnswer_DeveloperTool = 1, secondAnswer_DeveloperTool = 1):
    # testing_DeveloperTool = False
    # turn = 111
    # firstAnswer_DeveloperTool = 1
    # secondAnswer_DeveloperTool = 1
    if step == 1:
        print("""
            Menu:
                1. Set your Army.
                2. Battle!
        """)
        
        if testing_DeveloperTool == True:
            ans = firstAnswer_DeveloperTool
        else: ans = ""
        
        while ans != 1 and ans != 2:
        
            ans = int(input("Choose (1/2): "))
            if ans != 1 and ans != 2:
                print("""
            Menu:
                1. Set your Army.
                2. Battle!
                    
                ENTER "1" OR "2"
        """)
                
        if ans == 2:
            print("Turn", turn)
            # CALL NEXT TURN BATTLE -and update batallion ---------------------------------------------
        else: step = 2
        
            
            
    if step == 2:   
        #  CALL BASIC ARMY SETUP if turn == 1 or UPDATE BATALLIONS IF turn > first one-------------
        print("""
        Settings for Targaryen Army: 
            1. Queen assignment.
            2. Choose batallions
            3. Batallion order
            4. Attack mode
            5. Location
            6. Change all the above
            -----------------------
            0. Back to main menu""")
        
        if testing_DeveloperTool == True: # makes testing easier
            ans = secondAnswer_DeveloperTool
        else: ans = ""
        
        answers = (0,1,2,3,4,5,6)
        
        while ans not in answers:
        
            ans = int(input("Choose (1 to 6): "))
            if ans not in answers:
                print("""
        Settings for Targaryen Army: 
            1. Queen assignment.
            2. Choose batallions
            3. Batallion order
            4. Attack mode
            5. Location
            6. Change all the above
            -----------------------
            0. Back to main menu
            
            ENTER A NUMBER FROM "1" TO "6" """)
        
        if ans == 1:
            0
            #CALL QUEEN ASSIGNMENT
            menuDisplay(turn=turn, step = 2)
        elif ans == 2:
            0
            #CALL CHOOSE BATALLIONS
            menuDisplay(turn=turn, step = 2)
        elif ans == 3:
            0
            #CALL CHOOSE BATALLION ORDER
            menuDisplay(turn=turn, step = 2)
        elif ans == 4:
            0
            #CALL CHOOSE ATTACK MODE
            menuDisplay(turn=turn, step = 2)
        elif ans == 5:
            0
            #CALL CHOOSE LOCATION
            menuDisplay(turn=turn, step = 2)
        elif ans == 6:
            0
            #CALL ALL OF THE ABOVE
            menuDisplay(turn=turn, step = 2)
        elif ans == 0:
            menuDisplay(turn=turn)
            
    
# menuDisplay(1)

# # SETUP OF TARGARYEN ARMY #########################################################


# import random
# from map import Map
# from army import Army
# from batallion import Batallion
# from character import Character

# mapTargaryen = Map()
# targaryenArmy = Army()

# queenDaenerys = Character("queen", 500, name = "Daenerys", fixed_bonus = 50)




















