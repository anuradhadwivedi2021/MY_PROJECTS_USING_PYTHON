import random
import time

# Quiz Data (category wise)
quiz_data = {
    "Python": [
        {"question": "Which keyword is used to define a function in Python?", 
         "options": ["A. def", "B. func", "C. function", "D. define"], 
         "answer": "A"},
        {"question": "What is the output of: len('ChatGPT')?", 
         "options": ["A. 5", "B. 6", "C. 7", "D. 8"], 
         "answer": "C"}
    ],
    "General Knowledge": [
        {"question": "Which planet is known as the Red Planet?", 
         "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"], 
         "answer": "B"},
        {"question": "Who is the father of Computer Science?", 
         "options": ["A. Charles Babbage", "B. Alan Turing", "C. Tim Berners-Lee", "D. John von Neumann"], 
         "answer": "B"}
    ]
}

def quiz():
    print("🎯 Welcome to the Advanced Quiz Application 🎯")
    user_name = input("Enter your name: ")
    print(f"\nHello {user_name}, get ready to test your knowledge!\n")

    # Select Category
    print("Available Categories:")
    for i, category in enumerate(quiz_data.keys(), 1):
        print(f"{i}. {category}")

    choice = int(input("\nChoose a category number: "))
    category = list(quiz_data.keys())[choice - 1]
    questions = quiz_data[category]
    random.shuffle(questions)  # Randomize

    score = 0
    total = len(questions)

    # Ask Questions
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        start_time = time.time()
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        end_time = time.time()

        # Timer check
        if end_time - start_time > 10:  # 10 sec limit
            print("⏰ Time up! No marks awarded.")
            continue

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct Answer: {q['answer']}")

    # Final Result
    percentage = (score / total) * 100
    print("\n📊 Final Result 📊")
    print(f"Name: {user_name}")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")
    if percentage >= 50:
        print("🎉 Status: PASS")
    else:
        print("⚠ Status: FAIL")

    # Save Highscore
    with open("highscore.txt", "a") as f:
        f.write(f"{user_name} - {score}/{total} ({percentage:.2f}%)\n")

# Run Quiz
quiz()