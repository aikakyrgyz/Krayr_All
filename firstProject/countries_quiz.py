from rich import pretty
from rich import print
import random
# # reading files in CVS format
# # ----- cvs file contents:
# # Hostname, vendor, model, location
# # Sw1, Cisco, 4355, London
# # Sw2, Cisco, 4324, Amsterdam
# # Sw3, Cisco, 4667, Brazil
# ######
#
# import csv
#
# with open('csv_file.csv', 'r') as my_file:
#     reader = csv.reader(my_file)  # reader -  this is an iterator
#     for row in reader:
#         print(row)
# # Output:
# # ['Hostname', ' vendor', ' model', ' location']
# # ['Sw1', ' Cisco', ' 4355', ' London']
# # ['Sw2', ' Cisco', ' 4324', ' Amsterdam']
# # ['Sw3', ' Cisco', ' 4667', ' Brazil']
#
#
# # получаем заголовки столбоцов
#
#
# import csv
#
# with open('csv_file.csv', 'r') as my_file:
#     reader = csv.reader(my_file)  # reader -  this is an iterator
#     header = next(reader)
#     print('Headers:', header)
#     for row in reader:
#         print(row)
#
# # # Output
# # Headers: ['Hostname', ' vendor', ' model', ' location']
# # ['Sw1', ' Cisco', ' 4355', ' London']
# # ['Sw2', ' Cisco', ' 4324', ' Amsterdam']
# # ['Sw3', ' Cisco', ' 4667', ' Brazil']
#
#
# # creating a dict
# import csv
#
# with open('csv_file.csv', 'r') as my_file:
#     reader = csv.DictReader(my_file)  # reader -  this is an iterator
#     for row in reader:
#         print(row)
#         print(row['Hostname'], row[' model'])
#
# # Output
# # {'Hostname': 'Sw1', ' vendor': ' Cisco', ' model': ' 4355', ' location': ' London'}
# # Sw1  4355
# # {'Hostname': 'Sw2', ' vendor': ' Cisco', ' model': ' 4324', ' location': ' Amsterdam'}
# # Sw2  4324
# # {'Hostname': 'Sw3', ' vendor': ' Cisco', ' model': ' 4667', ' location': ' Brazil'}
# # Sw3  4667
#
# # writing to csv file:
#
# data = [['Hostname', ' vendor', ' model', ' location'],
#         ['Sw1', ' Cisco', ' 4355', ' London'],
#         ['Sw2', ' Cisco', ' 4324', ' Amsterdam'],
#         ['Sw3', ' Cisco', ' 4667', ' Brazil']]
#
# with open('new_cvs_file.csv', 'w+') as myfile:
#     writer = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)  # puts all the values in quotes
#     for row in data:
#         writer.writerow(row)
#         # or just writing without a loop
#     writer.writerows(data)
#     myfile.seek(0)
#     print(myfile.read())
#
# # Output:
# # Hostname, vendor, model, location
# # Sw1, Cisco, 4355, London
# # Sw2, Cisco, 4324, Amsterdam
# # Sw3, Cisco, 4667, Brazil
#
# list_ = ['1\n', '2\n']
# write('1\n 2\n')
# write(list_)
# writelines(list_)
#
# # JSON
#
# # reading a file from json format .json.load()
#
# import json
#
# with open('jason_file.json', 'r') as myfile:
#     templates = json.load(f)
#
# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f'Question: {self.text}\nAnswer: {self.answer}'


class QuizGame:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.strike = 0
        self.q_list = question_list
        random.shuffle(question_list)

    def next_question(self):
        current_q = self.q_list[self.question_number]
        self.question_number += 1
        user_answer = input(current_q.text)
        # hint_answer = ''
        # hint_index = 0
        # if user_answer.strip().lower == 'hint':
        #     while user_answer.strip().lower() != 'pass':
        #         hint_answer += current_q.answer[hint_index]
        #         print(f"Hint! The first {hint_index+1 if hint_index!=0 else ''} {'letter is' if hint_index==0 else 'letters are'} {hint_answer}")
        #         user_answer = input(current_q.text)

        self.correct(user_answer, current_q)

    def correct(self, user_answer, question):
        if question.answer.lower() == user_answer.strip().lower():
            print(f'Correct! The capital is indeed {question.answer}')
            if self.strike == 3:
                print('Strike! 3 questions answered right in a row!')
                print('Score boost!')
                self.score += 3
                self.strike = 0
            else:
                self.score += 1
            print('Score now is: ', self.score)
        else:
            print('Sorry! Wrong. The correct answer was:', question.answer)

    def more_questions(self):
        return self.question_number < len(self.q_list)


def create_questions():
    import csv
    list_of_questions = []
    with open('country_list.csv') as file:
        reader = csv.DictReader(file)  # reader -  this is an iterator
        header = next(reader)
        # print('Headers:', header)
        for row in reader:
            list_of_questions.append(Question('What is the capital of ' + row['country'] + '? ', row['capital']))

    return list_of_questions



print(1)
my_quiz = QuizGame(create_questions())
while my_quiz.more_questions():
    # print('Attention: If you do not know the answer enter (hint) and we will provide you a hint!\nEnter (pass) if you want to pass the question')
    my_quiz.next_question()