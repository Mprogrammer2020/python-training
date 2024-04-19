'''
Task: Create a simple rock, paper, scissor game

Requirements:
1. First take user input to choose either 'rock', 'paper' or 'scissor'
2. Then computer will automatically choose either 'rock', 'paper' or 'scissor'
3. If user wins, then print "You win", if computer wins, then print "You lose"
4. If it's a tie, then again take user input and play the game again until user or computer wins

Rules:
1. rock beats scissor
2. paper beats rock
3. scissor beats paper

Test Case:
1. User can only choose from 'rock', 'paper' or 'scissor'
'''

# Write your code here
import random

def rock_paper_scissors():
    while True:
        # Take user input
        user_choice = input("Enter 'rock', 'paper', or 'scissor': ")
        
        # Validate user input
        if user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissor'.")
            continue
        
        # Computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissor'])
        print("Computer chose:", computer_choice)
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You win!")
            break
        else:
            print("You lose!")
            break

# Test the game
rock_paper_scissors()