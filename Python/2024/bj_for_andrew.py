"""
Name: blacjack.py
Author:  Andrew Peterson
Created:  08/25/2024
Purpose: play blackjack
"""

import random

player_total = 0
dealer_total = 0
# TODO: ask player for there bet
bet = float(input("How much would you like to bet? "))
print("-------------------------------------------------")
# TODO: use a list to create a digital card deck
deck = [10] * 16  # 4 types of 10s jacks queens and kings
[deck.extend([n] * 4) for n in range(1, 10)]  # add the rest 4 types of aces and 2-9
# TODO: ask player to hit or stay
# I asked an AI to remind me of some of the diffrent lopes
while True:
    choice = input("(H)it or (S)tay? ").strip().lower()
    print("-------------------------------------------------")
    # had the AI Remind my about if then statements
    if choice == "h":  # player plays when his choice is h
        card = random.choice(deck)
        if player_total < 11 and card == 1:  # if ace and total < 11 count it as 11
            card = 11
        print(f"Your card: {card}")
        player_total += card
        print(f"Player Total: {player_total}")
        print("-------------------------------------------------")
        if card == 11:
            card = 1
        deck.remove(card)
        if player_total > 20:  # if it's 21 or over the game is over
            break
    elif dealer_total > 16:  # if no hit and dealer has more than 16, the game is over
        break
    if dealer_total < 17:
        card = random.choice(deck)
        if dealer_total < 11 and card == 1:
            card = 11
        print(f"The Dealers card: {card}")
        dealer_total += card
        print(f"Dealer Total: {dealer_total}")
        print("-------------------------------------------------")
        if card == 11:
            card = 1
        deck.remove(card)
        if dealer_total > 20:  # if it's 21 or over the game is over
            break
# TODO: draw card a remove it from list
# TODO: add to the value of the player or dealer
# TODO: Inform the player they have lost if they go over 21 or if they are under dealer
if (
    player_total > 21
    or (dealer_total < 22 and player_total < dealer_total)
    or dealer_total == 21
):
    print(f"sorry, you lose {bet} dollars")
elif player_total == dealer_total:
    print("Tie, you get back your Ante")
else:
    print(f"Congratulations, you win {bet} dollars")
