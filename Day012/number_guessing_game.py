from random import randint

EASY = 10
HARD = 5
MAX_NUM = 100
MIN_NUM = 1

logo = '''
 _____                       _____ _            _   _                 _               
|  __ \                     |_   _| |          | \ | |               | |              
| |  \/_   _  ___  ___ ___    | | | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/   \_/ |_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|  
'''

print(logo)
print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {MIN_NUM} and {MAX_NUM}.")
num = randint(MIN_NUM, MAX_NUM)
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = EASY if choice == "easy" else HARD

# test num
# print(f"Psssst the answer is {num}")

def check_answer(guess, num):
    result = True
    if guess == num:
        print(f"You got it! The answer was {num}.")
        return False
    elif guess > num:
        print("Too high.")
    else:
        print("Too low")

    return result

continue_game = True
while continue_game:
    print(f"You have {attempts} attempt/s to guess the number.")
    guess = int(input("Make a guess: "))
    continue_game = check_answer(guess, num)
    
    attempts -= 1

    if continue_game:
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses. You lose.")
            continue_game = False