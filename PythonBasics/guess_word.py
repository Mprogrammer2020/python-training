
actual_word = "Abhishek"
given_word = "A-hi--e-"

def guess_word(actual_word, given_word):
    lives = 5
    guessed_letters = set()
    incorrect_guesses = []

    print("Complete the word by filling the blanks:")
    print(given_word)

    while lives > 0 and given_word != actual_word:
        # Get user input
        user_input = input("Enter a letter: ").lower()

        # Validate input
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if user_input in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        if user_input in actual_word.lower():
            guessed_letters.add(user_input)
            # Update the given word
            for i in range(len(actual_word)):
                if actual_word[i].lower() == user_input:
                    given_word = given_word[:i] + actual_word[i] + given_word[i + 1:]
            print("You guessed its correct:", given_word)
        else:
            if user_input not in guessed_letters:
                guessed_letters.add(user_input)
                incorrect_guesses.append(user_input) 
            lives -= 1
            print(f"You guessed a wrong alphabet. {lives} lives left.")

    # all guess wrong
    if lives == 0:
        print("You lost! The word was:", actual_word)
    else:
        print("You won! You guessed the complete word:", actual_word)

guess_word(actual_word, given_word)
