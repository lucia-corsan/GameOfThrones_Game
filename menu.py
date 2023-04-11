# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:04:10 2020

@author: lucia
"""


# MENU
def menuDisplay(turn, step = 1, testing_DeveloperTool = False, firstAnswer_DeveloperTool = 1, secondAnswer_DeveloperTool = 1):
    #DeveloperTool attributes are a way for the developer to check that everything works fine; explained in detail in the report.
    
    if step == 1: #first part of the menu displayed
        print("""
            Menu:
                1. Set your Army.
                2. Battle!
        """)
        
        if testing_DeveloperTool == True:
            ans = firstAnswer_DeveloperTool
        else: ans = ""
        
        while ans != 1 and ans != 2:
        
            ans = int(input("Choose (1/2): ")) #asks for a number again
            if ans != 1 and ans != 2: #if not, the game displays the main menu again
                print("""
            Menu:
                1. Set your Army.
                2. Battle!
                    
                ENTER "1" OR "2"
        """)
                
        if ans == 2:
            print("Turn", turn)
###            # CALL NEXT TURN BATTLE -and update batallion ---------------------------------------------
        else: step = 2
        
            
            
    if step == 2:   
###        #  CALL BASIC ARMY SETUP if turn == 1 or UPDATE BATALLIONS IF turn > first one-------------
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
        
        if testing_DeveloperTool == True:
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
