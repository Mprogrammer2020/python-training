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
import random

possible_actions = ["rock", "paper", "scissors"]
# validate the user action
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower() 
    if user_action in possible_actions:
        break  
    else:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print(" You win! ")
    else:
        print("You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print(" You win!")
    else:
        print("You lose.")
