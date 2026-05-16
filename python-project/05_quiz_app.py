questions_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    }
]

def run_quiz(question):
    score = 0

    for q in question:
        print("\n" + q["question"])
        for option in q["question"]:
            print(option)


            user_answer = input("Enter Your Choice:").upper()


            if user_answer == q["answer"]:
                print("correct!")
                score += 1
            else:
                print(f"Incorrect.The correct answer was {q["answer"]}")

        print("\n quiz completed")
        print(f"Your final score is: {score} out of {len(question)} question correct.")

if __name__ == "__main__":
    run_quiz(questions_data)