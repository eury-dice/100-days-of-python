import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
cpu_choice = random.randint(0,2)

#when user input is not within [0 - 2], you automatically lose
if ((user_choice > 2) or (user_choice < 0)):
    user_choice = 0 #Rock
    cpu_choice = 1  #Scissors

print(options[user_choice] + '\nComputer chose:\n' + options[cpu_choice])

if (user_choice == cpu_choice):
    print('Draw.')
elif (
            ((user_choice == 0) and (cpu_choice == 2)) 
        or  ((user_choice == 1) and (cpu_choice == 0)) 
        or  ((user_choice == 2) and (cpu_choice == 1))
     ):
    print('You win!')
else:
    print('You lose')