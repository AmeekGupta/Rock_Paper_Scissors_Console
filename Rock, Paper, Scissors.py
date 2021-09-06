# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:16:46 2021

Game -- Rock, Paper, Scissors

@author: ameek
"""
import random # Importing random
possible_input = ['rock', 'paper', 'scissors'] # Generating list of options
user_count = 0 # For user scoring
comp_count = 0 # For computer scoring

while True:
    computer_choice = random.choice(possible_input) # Randomizing computer choices
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower() # User input
    if user_choice == computer_choice: # Both chose same choice
        print(f"\nBoth players have chosen {user_choice}, it's a tie!")

    elif user_choice == 'rock': # User chose rock
        if computer_choice == 'paper':
            print("\nI chose PAPER! I win!")
            comp_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
        else:
            print("\nI chose SCISSORS! YOU WIN!")
            user_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
    elif user_choice == 'paper': # User chose paper
        if computer_choice == 'rock':
            print("\nI chose ROCK! YOU WIN!")
            user_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
        else:
            
            print("\nI chose SCISSORS! I win!")
            comp_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
    elif user_choice == 'scissors': # User chose scissors
        if computer_choice == 'rock':
            print("\nI chose ROCK! I win!")
            comp_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
        else:
            print("\nI chose PAPER! YOU WIN!")
            user_count += 1
            print(f"Computer: {comp_count}, Player: {user_count}")
    else:
        print("\nPlease check your spelling and try again!") # For spelling mistake
    play_again = input("Play again? (y/n): ").lower() # Prompting player to play or exit
    if play_again != 'y':
        break
