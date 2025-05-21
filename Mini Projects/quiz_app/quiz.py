class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
                "correct": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                "correct": "B"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
                "correct": "B"
            }
        ]
        self.score = 0

    def display_question(self, question_data):
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)
        return input("Enter your answer (A/B/C/D): ").upper()

    def run_quiz(self):
        print("Welcome to the Quiz App!")
        print("Answer the following questions:")
        
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}:")
            answer = self.display_question(question)
            
            if answer == question["correct"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct']}")
        
        self.display_final_score()

    def display_final_score(self):
        total_questions = len(self.questions)
        print(f"\nQuiz completed! Your score: {self.score}/{total_questions}")
        percentage = (self.score / total_questions) * 100
        print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz() 