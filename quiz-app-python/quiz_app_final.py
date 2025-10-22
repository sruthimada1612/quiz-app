import random
import time

# -------------------------------
# QUIZ QUESTIONS DATABASE
# -------------------------------
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "Who developed the Python programming language?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which data structure uses FIFO (First In, First Out)?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "What does SQL stand for?",
        "options": ["Structured Query Language", "Strong Question Language", "Simple Query Logic", "Sequential Query Language"],
        "answer": "Structured Query Language"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["//", "#", "/* */", "<!-- -->"],
        "answer": "#"
    },
    {
        "question": "Which company developed Java?",
        "options": ["Microsoft", "Apple", "Sun Microsystems", "IBM"],
        "answer": "Sun Microsystems"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["Tuple", "List", "String", "Integer"],
        "answer": "List"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".txt", ".py", ".exe", ".java"],
        "answer": ".py"
    }
]

# -------------------------------
# RUN QUIZ FUNCTION
# -------------------------------
def run_quiz(username):
    while True:
        print(f"\n🎯 Welcome, {username}! Let's start the quiz.\n")
        score = 0

        # Randomize the order of questions
        questions = random.sample(quiz_questions, len(quiz_questions))

        for index, q in enumerate(questions, 1):
            print(f"\nQuestion {index}: {q['question']}")
            options = q["options"]
            random.shuffle(options)

            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            while True:
                try:
                    answer = int(input("Your answer (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("Please choose a valid option (1-4).")
                except ValueError:
                    print("Enter a number between 1 and 4.")

            if options[answer - 1] == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")

            time.sleep(0.5)

        # Final score
        print("\n===============================")
        print(f"🎉 Quiz Completed, {username}!")
        print(f"Your Final Score: {score}/{len(questions)}")
        print("===============================")

        # Save score to file
        with open("scores.txt", "a") as file:
            file.write(f"{username} - {score}/{len(questions)}\n")

        # Post-quiz options
        while True:
            print("\nWhat would you like to do next?")
            print("1. Retake the Quiz")
            print("2. Go Back to Main Menu")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ").strip()

            if choice == "1":
                break  # Retake (restart the loop)
            elif choice == "2":
                return  # Go back to main menu
            elif choice == "3":
                print("👋 Thanks for playing! Goodbye!")
                input("\nPress Enter to exit...")
                exit()
            else:
                print("❌ Invalid choice, please try again.")


# -------------------------------
# MAIN MENU FUNCTION
# -------------------------------
def main_menu():
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Start Quiz")
        print("2. View Previous Scores")
        print("3. Exit")
        print("===============================")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            username = input("Enter your name: ").strip().title()
            run_quiz(username)

        elif choice == "2":
            print("\n--- Previous Scores ---")
            try:
                with open("scores.txt", "r") as file:
                    scores = file.readlines()
                    if scores:
                        for line in scores:
                            print(line.strip())
                    else:
                        print("No scores recorded yet.")
            except FileNotFoundError:
                print("No scores recorded yet.")

        elif choice == "3":
            print("👋 Thanks for playing! Goodbye!")
            input("\nPress Enter to exit...")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# -------------------------------
# START PROGRAM
# -------------------------------
if __name__ == "__main__":
    print("===================================")
    print("        🧠 Python Quiz App         ")
    print("===================================")
    main_menu()

