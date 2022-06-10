
import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
game_over = False
end_message = "You lose."
chosen_word = random.choice(word_list)

display = ["_" for _ in chosen_word]

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

print("\n" + " ".join(display))
print(stages[lives])

while not game_over:

    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You already guessed {guess}.")
    elif guess not in chosen_word:
        print(f"You guessed {guess}. Sorry, it's not in the word.")
        lives -= 1
        if(lives == 0):
            game_over = True

    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            display[index] = guess
    

    if "_" not in display:
        game_over = True
        end_message = "You win!"

    print("\n" + " ".join(display))
    print(stages[lives])
        
print(end_message)