def guess_word():
    actual_word = "Abhishek"
    given_word = "abhi--e-"
    lives = 5
    hidden_word = {a for a, b in zip(actual_word.lower(), given_word.lower()) if b == "-"}
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