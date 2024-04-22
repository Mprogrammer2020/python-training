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

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return "tie"
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "paper" and computer_action == "rock") or \
         (user_action == "scissors" and computer_action == "paper"):
        return "user"
    else:
        return "computer" 

# Validate the user action
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower() 
    if user_action in possible_actions:
        break  
    else:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# Computer selects an action randomly
computer_action = random.choice(possible_actions)
print(f"Computer chooses {computer_action}.")

# Determine the winner
winner = determine_winner(user_action, computer_action)
if winner == "tie":
    print("It's a tie!")
elif winner == "user":
    print("You win!")
else:
    print("You lose!")
