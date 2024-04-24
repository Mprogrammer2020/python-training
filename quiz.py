'''
Create a KBC game

- There will be total 5 questions. Each question will have 4 options and one correct answer.
- If user answer with any wrong option, then the game will be over, Otherwise user will be allowed to move to next question.
- There will be 2 lifelines available in game.
    1) 50-50
    2) Audience Poll
- If user have used a lifeline, that will be unavailable for next questions.
- User can exit the game anytime by typing "exit", if they don't want to answer or play.
- The game will automatically give Rs.10000 for each correct answer, if they give any wrong answer, then they will get nothing.
- When they exit the game, they will get the total amount they have earned till that point.
'''


import random
def play_kbc():
    questions = [
        {"question": "What is the capital of India?",
         "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
         "answer": 0},
        {"question": "Which river is known as the 'Sorrow of Bengal'?",
         "options": ["Ganga", "Yamuna", "Brahmaputra", "Godavari"],
         "answer": 2},
        {"question": "In which sport does Saina Nehwal excel?",
         "options": ["Cricket", "Hockey", "Badminton", "Tennis"],
         "answer": 2},
        {"question": "What is the currency of Japan?",
         "options": ["Rupee", "Yuan", "Yen", "Dollar"],
         "answer": 2},
        {"question": "Mount Everest is located in:",
         "options": ["India", "Nepal", "China", "Bhutan"],
         "answer": 1},
    ]

    lifelines = {
        "50-50": True,
        "Audience Poll": True,
    }

    current_question = 0
    earnings = 0

    while current_question < len(questions):
        question = questions[current_question]

        print(f"Question {current_question + 1}: {question['question']}")
        for i in range(len(question["options"])):
            print(f"  {i + 1}. {question['options'][i]}")

        answer = input("Enter your answer (1-4) or 'exit' to quit, 'lifeline' to use one: ")

        if answer == "exit":
            print(f"Thank you for playing! You earned Rs. {earnings}.")
            break
        elif answer == "lifeline":
            lifeline_choice = input("Which lifeline would you like to use? (50-50 or Audience Poll): ")
            if lifeline_choice not in lifelines:
                print("Invalid lifeline choice. Please choose between '50-50' and 'Audience Poll'.")
                continue
            if use_lifeline(lifelines, questions, current_question, lifeline_choice):
                continue  
            else:
                print("You've already used both lifelines.")
                continue
        else:
            try:
                answer = int(answer) - 1
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

        if answer == question["answer"]:
            print("Correct!")
            earnings += 10000
            current_question += 1
        else:
            print("Incorrect. You earned Rs. 0 this round.")
            break

def use_lifeline(lifelines, questions, current_question, lifeline_choice):
    if not lifelines[lifeline_choice]:
        return False

    print(f"Using lifeline: {lifeline_choice}")

    if lifeline_choice == "50-50":
    
        incorrect_options = []
        for i in range(len(questions[current_question]["options"])):
            if i != questions[current_question]["answer"]:
                incorrect_options.append(i)
        removed_options = random.sample(incorrect_options, 2)
        lifelines["50-50"] = False
        print("Remaining options:")
        for i in range(len(questions[current_question]["options"])):
            if i not in removed_options:
                print(f"  {i + 1}. {questions[current_question]['options'][i]}")
    else:
        # Audience poll
        votes = [1, 1, 1, 1]  
        votes[questions[current_question]["answer"]] += 3
        total_votes = sum(votes)
        print("Audience Poll results:")
        for i in range(len(questions[current_question]["options"])):
            percentage = round((votes[i] / total_votes) * 100, 1)
            print(f"  {questions[current_question]['options'][i]}: {percentage}%")

    return True

if __name__ == "__main__":
    play_kbc()
