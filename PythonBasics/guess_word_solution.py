'''
actual_word = "Abhishek"

given_word = "abhi--e-"

- User can only see the given word
- Take single alphabet input from user and put it in the place if it is in the given word
- User will have 5 lives
- If user guesses the wrong alphabet, then he will lose a life
- If user enter any word that is already guessed, then he will lose a life
- If user chooses any word that cannot be filled in the blanks, then he will lose a life
- End the game when the lives are over or when user guess the complete word.

Example:
Complete the word by filling the blanks: Abhi-e-

If user enter 'k', then: You guessed the correct alphabet: Abhi-ek

If user enter 'l', then: You guessed a wrong alphabet, 4 lives left

If user enter 'a', then: You guessed a wrong alphabet, 3 lives left

If again user enter 'k', then: You guessed a wrong alphabet, 2 lives left

If user enter 'h', then: You guessed the correct alphabet: Abhihek

If user guesses the word: You won, You guessed the complete word: Abhishek

'''

def guess_word():
    actual_word ="abhishek"
    given_word = "abhi----"
    lives = 5
    hidden_word = {a for a, b in zip(actual_word.lower(), given_word.lower()) if b == "-"}
    #print(hidden_word)
    print("Complete the word by filling the blanks:", given_word)
    while lives > 0:
        user_input = input("Enter a letter: ").lower()
        if user_input in hidden_word:
            hidden_word.remove(user_input)
            for i in range(len(actual_word)):
                if actual_word[i].lower() == user_input:
                    given_word = given_word[:i] + actual_word[i] + given_word[i+1:]
            if given_word.lower() == actual_word.lower():
                print("You won!, You guessed the complete word:", actual_word)
                break
            print("You guessed the correct alphabet:", given_word)
        else:
            lives -= 1
            print("You guessed a wrong alphabet, ", lives, "lives left")

guess_word()