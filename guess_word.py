'''
actual_word = "Abhishek"

given_word = "ab-i--e-"

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
actual_word = "Abhishek"
given_word = "Ab-i--e-"

def guess_word(actual_word, given_word):
    lives = 5
    guessed_letters = set()  
    incorrect_guesses = []  

    print("Complete the word by filling the blanks:")
    print(given_word)

    while lives > 0 and given_word != actual_word:
        
        user_input = input("Enter a letter: ").lower()

        # Validate input
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if user_input in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(user_input)  

        if user_input.lower() in actual_word.lower():
            # Update the given word 
            for i in range(len(actual_word)):
                if actual_word[i] == user_input:
                    given_word = given_word[:i] + actual_word[i] + given_word[i + 1:]
            print("You guessed the correct letter:", given_word)
        else:
            lives -= 1
            incorrect_guesses.append(user_input)
            print(f"You guessed a wrong letter. {lives} lives left. Incorrect guesses: {', '.join(incorrect_guesses)}")
    # all guess wrong
    if lives == 0:
        print("You lost! The word was:", actual_word)
    else:
        print("You won! You guessed the complete word:", actual_word)

guess_word(actual_word, given_word)
