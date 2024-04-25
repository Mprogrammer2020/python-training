'''
actual_word = "Abhishek"

given_word = "Ab-i--e-"

- User can only see the given word
- Take single alphabet input from user and put it in the place if it is in the given word
- User will have 5 lives
- If user guesses the wrong alphabet, then he will lose a life
- If user enter any word that is already guessed, then he will lose a life
- If user chooses any word that cannot be filled in the blanks, then he will lose a life
- End the game when the lives are over or when user guess the complete word.

Example:
Complete the word by filling the blanks: Ab-i-e-

If user enter 'k', then: You guessed the correct alphabet: Ab-i-ek

If user enter 'l', then: You guessed a wrong alphabet, 4 lives left

If user enter 'a', then: You guessed a wrong alphabet, 3 lives left

If user guesses the word: You won, You guessed the complete word: Abhishek
'''