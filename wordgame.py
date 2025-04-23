import random

class QuizGame:
    def _init_(self):
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Berlin', 'Paris', 'Madrid', 'Rome'],
                'correct_answer': 'Paris',
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Mercury'],
                'correct_answer': 'Mars',
            },
            {
                'question': 'What is the largest mammal?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale',
            },
        ]
        self.score = 0

    def ask_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ")
        return question['options'][int(user_answer) - 1]

    def play_game(self):
        random.shuffle(self.questions)

        for question in self.questions:
            user_choice = self.ask_question(question)

            if user_choice == question['correct_answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}.\n")

        self.display_final_score()

    def display_final_score(self):
        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")

if _name_ == "_main_":
    print("Welcome to the Quiz Game!\n")
    game = QuizGame()
    game.play_game()