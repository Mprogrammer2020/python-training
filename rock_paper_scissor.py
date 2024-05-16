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
def play_rock_paper_scissors():
  
  possible_action = ["rock", "paper", "scissors"]

  while True:
    # Get user input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user input
    if user_choice not in possible_action:
      print("Invalid choice. Please choose rock, paper, or scissors.")
      continue
    computer_choice = random.choice(possible_action)

    # Determine the winner
    if user_choice == computer_choice:
      print("It's a tie! play again.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
      print("You win. The computer chose", computer_choice)
      return
    else:
      print("You lose. The computer chose", computer_choice)
      return

play_rock_paper_scissors()

