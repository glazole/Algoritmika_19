#!/usr/bin/env python
import os
import csv

import django
import sys


sys.path.append('/home/leader_19/recomendation/') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'recomendation.settings'
django.setup()

from app.models import Question, Choice, UserId


N_QUEST = 22
N_ANS = 132

with open('users.csv', 'r', encoding='utf-8') as users:
    users_list = []
    file_reader = csv.reader(users, delimiter=',')
    for row in file_reader:
        users_list.append(row)

print("done")
for i in range(1, 501): #len(users_list)+1):
    user = UserId.objects.create(
        username=users_list[i][0],
	password=users_list[i][0],
        added_at=users_list[i][1],
        sex=users_list[i][2],
        birth_date=users_list[i][3],
        address=users_list[i][4],
    )
#    print("User {} added".format(i))
print("done2")

with open('list_questions.csv', 'r', encoding='cp1251') as questions:
    question_list = []
    file_reader = csv.reader(questions) #, delimiter=';')
    for row in file_reader:
        question_list.append(row)
    print(question_list)


with open('list_answers.csv', 'r', encoding='utf_8') as choices:
    choice_list = []
    file_reader = csv.reader(choices, delimiter=',')
    for row in file_reader:
        choice_list.append(row)
    print(choice_list)


for i in range(1, N_QUEST+1):
    question = Question.objects.create(
        question_text=question_list[i],
    )
    print("Question {} added".format(i))
   
for i in range(1, N_ANS+1):
    for j in range(1, int(N_ANS/N_QUEST)+1):
        choice = Choice.objects.create(
        question=Question.objects.get(id=i),
        choice_text=choice_list[j][1],
        votes=choice_list[j][2],
            )
        print("Choice {} added".format(j))
    print("Question {} close".format(i))
