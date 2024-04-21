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

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")