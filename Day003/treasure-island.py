print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input('You find yourself in front of two passageways, one to the left and the other to the right.\nDo you go (left / right)? ')
if(choice.lower() == 'left'):
    choice = input("You walk through a long passageway and find an underground river. There are signs indicating that there is a boat that travels the river. You don't know how long you'll have to wait for its return. The river seems calm, with nary a ripple in its waters. Do you (swim / wait)? ")
    if(choice.lower() == 'wait'):
        choice = input('A few minutes pass when the boat arrives. The boatman is a hooded figure, silent as the grave. He ferries you to a place with three doors. The leftmost is bright red, the color of fresh blood. The center door is a wooden yellow door, its paint peeling at its hingers. The rightmost door is a metallic blue, you see your reflection staring right back at you. Do you choose the (red / yellow / blue) door? ')
        if(choice.lower() == 'red'):
            print('As you enter the room, the door closes firmly behind you. Before you can react, fire rains down and burns you to ash. GAME OVER.')
        elif(choice.lower() == 'yellow'):
            print('The yellow door creaks as you open it, within it lies a golden room, filled with the lost treasures of the world. You have succeeded in finding the treasure! SUCCESS.')
        elif(choice.lower() == 'blue'):
            print('You open the door to find a large vault. Hurriedly, you open it and find a maiden within it. She looks at you and smiles. You are left unable to move as her glare freezes you from the feet up. Your body shatters to a million pieces as the maiden closes the vault once more. GAME OVER.')
        else:
            print('You suddenly feel a prick on your neck. A poisonous needle by the looks of it. Your vision warps your surroundings and you fall to the ground, cold and unmoving. GAME OVER.')
    else:
        print('You find yourself diving into the river, its water ice cold. You begin swimming when you realize the surrounding waters darkening. A giant sea serpent surfaces and devours you whole. GAME OVER.')
else:
    print('As you walk through the passageway, the ground crumbles underneath you and you get impaled by the stalagmites underneath. GAME OVER.')

