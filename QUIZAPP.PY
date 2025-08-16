import random

# Questions with options and correct answers
quiz_questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "3. Which data structure uses FIFO (First In First Out)?",
        "options": ["A. Stack", "B. Queue", "C. Array", "D. Tree"],
        "answer": "B"
    },
    {
        "question": "4. Which one is not a programming language?",
        "options": ["A. HTML", "B. Python", "C. Java", "D. C++"],
        "answer": "A"
    },
    {
        "question": "5. What is 5 + 7?",
        "options": ["A. 11", "B. 12", "C. 13", "D. 14"],
        "answer": "B"
    }
]

# Shuffle questions (randomization)
random.shuffle(quiz_questions)

score = 0

print("🎯 Welcome to the Quiz Game!")
print("Answer by typing A, B, C, or D\n")

for q in quiz_questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    answer = input("Your answer: ").strip().upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}\n")

print("🎉 Quiz Over!")
print(f"Your Score: {score}/{len(quiz_questions)}")