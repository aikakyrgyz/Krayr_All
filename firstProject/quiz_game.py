import csv
import random

####### QUIZ GAME #########

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __str__(self):
        return f'{self._text} -> {self._answer}'



def create_questions():
    list_of_questions = []
    with open('country_list.csv') as file:
        reader = csv.DictReader(file) # reader -> iterator -> pointer
        # first_row = next(reader) # moving to the next row each time you do next
        # second_row = next(reader)
        # third_row = next(reader)
        # print(first_row)
        for row in reader:
            # country = row['country']
            # capital = row['capital']
            question = Question(row['country'], row['capital'])
            list_of_questions.append(question)

    return list_of_questions

class QuizGame:
    def __init__(self, question_list):
        self.question_list = question_list
        random.shuffle(self.question_list)
        self.current_q_index = 0
        self.score = 0


    def next_question(self):
        '''Displays a question'''
        current_q = self.question_list[self.current_q_index]
        # print(current_q) # Abhazia -> Sukhumi
        user_answer = input(f'What is the capital of {current_q.text}?')
        self.correct(user_answer, current_q)
        self.current_q_index += 1

    def correct(self, user_answer, current_q):
        if user_answer.strip().lower() == current_q.answer.strip().lower():
            print(f'Correct! The capital is indeed {current_q.answer}')
            self.score += 1
        else:
            print(f'Sorry! Wrong. The capital was {current_q.answer}')
        print('Your current score is ', self.score)

    def more_questions(self):
        return self.current_q_index < len(self.question_list)



game = QuizGame(create_questions())

while game.more_questions():
    game.next_question()
