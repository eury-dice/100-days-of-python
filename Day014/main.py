from os import system
from art import logo, vs
from game_data import data
from random import shuffle

game_options = data
score = 0

def get_option(data):
    shuffle(data)
    return data.pop()

def check(opA, opB, choice):
    result = False
    if (
                ((choice == 'a') and (opA['follower_count'] >= opB['follower_count']))
            or  ((choice == 'b') and (opA['follower_count'] <= opB['follower_count']))
    ):
        result = True
    return result

keep_playing = True
system("cls")
print(logo)
while keep_playing:
    if score > 0:
        print(f"You're right! Current Score: {score}.")
        optionA = optionB
    else:
        optionA = get_option(game_options)
    print(f"Compare A: {optionA['name']}, {optionA['description']}, from {optionA['country']}")
    print(vs)
    optionB = get_option(game_options)
    print(f"Compare B: {optionB['name']}, {optionB['description']}, from {optionB['country']}")
    choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    
    system("cls")
    print(logo)

    if (check(optionA, optionB, choice)):
        score += 1
        if len(game_options) == 0:
            print(f"Congratulations, you got the highest possible score! Final Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        keep_playing = False