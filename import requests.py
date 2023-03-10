import requests
import json
import random

# Define a function to retrieve quiz questions from the Open Trivia Database API
def get(category, difficulty, num_questions):
    url = f"https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    print(response)
    data = json.loads(response.text)
    return data['results']

# Define a function to ask quiz questions and check answers
def ask_quiz_question(question, correct_answer, answers):
    # Present the question and answers to the user
    print(f"\nQuestion: {question}")
    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    # Prompt the user to input their answer and check if it is correct
    user_answer = input("Answer (enter a number): ")
    try:
        user_answer_index = int(user_answer) - 1
        user_answer = answers[user_answer_index]
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            return 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
            return 0
    except:
        print("Invalid input. Skipping question.")
        return 0

# Define the quiz parameters
category = 18 # Computer Science category
difficulty = "easy"
num_questions = 1

# Get quiz questions from the Open Trivia Database API
quiz_questions = get(category, difficulty, num_questions)

# Initialize the user's score to zero
score = 0

# Loop through the quiz questions and ask them
for quiz_question in quiz_questions:
    question = quiz_question['question']
    correct_answer = quiz_question['correct_answer']
    incorrect_answers = quiz_question['incorrect_answers']
    answers = incorrect_answers + [correct_answer]
    random.shuffle(answers)
    score += ask_quiz_question(question, correct_answer, answers)

# Present the user's final score
print(f"\nYou scored {score} out of {num_questions}.\n")
