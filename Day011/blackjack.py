from os import system
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

def change_ace(cards):
    #Changes ace (if there are any) from 11 to 1 if player/dealer is above 21
    score = sum(cards)
    while 11 in cards:
        ace = cards.index(11)
        cards[ace] = 1
        score -= 10
        if score < 22:
            break

    return cards, score


choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play = True if choice == 'y' else False

while play:
    system("cls")
    print(logo)
    
    player_cards = random.choices(cards, k=2)
    player_score = sum(player_cards)

    if(player_score > 21):
        player_cards, player_score = change_ace(player_cards)
    
    dealer_cards = random.choices(cards, k=2)
    dealer_score = sum(dealer_cards)
    
    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {dealer_cards[0]}")

    # Player's turn
    player_bust = False
    while not player_bust and player_score != 21 and dealer_score != 21:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == 'y':
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
        else:
            break
        
        if player_score > 21:
            player_cards, player_score = change_ace(player_cards)

        print(f"\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\tComputer's first card: {dealer_cards[0]}")

        if player_score > 21:
            player_bust = True
    
    # Dealer's Turn
    if dealer_score > 21:
        dealer_cards, dealer_score = change_ace(dealer_cards)

    while (dealer_score < 17) and player_score <= 21:
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(cards)

        if dealer_score > 21:
            dealer_cards, dealer_score = change_ace(dealer_cards)

    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_bust:
        print("You went over. You lose.")
    elif dealer_score > 21:
        print("Computer went over. You win!")
    elif player_score == 21:
        print("Blackjack! You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif dealer_score == 21:
        print("Computer got Blackjack. Sorry, you lose.")
    elif player_score < dealer_score:
        print("Sorry, you lose.")
    else: #Same Score
        if len(player_cards) == len(dealer_cards):
            print("DRAW")
        elif len(player_cards) < len(dealer_cards):
            print("You have the same score with less cards, you win!")
        else:
            print("Computer got the same score with less cards, you lose.")

    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    play = True if choice == 'y' else False