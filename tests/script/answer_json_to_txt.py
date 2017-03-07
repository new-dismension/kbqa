# coding:utf-8

import json


training_data = None
with open('datasets/training_data_kbq_0.json', 'r') as f:
    training_data = json.load(f)


testing_data = None
with open('datasets/testing_data_kbq_0.json', 'r') as f:
    testing_data = json.load(f)


answers = []

for i in training_data:
    is_kbq = i['is_kbq']
    if is_kbq:
        if type(is_kbq) == list:
            if not is_kbq[0]:
                continue

        answers.append(i['a'])


for i in testing_data:
    is_kbq = i['is_kbq']
    if is_kbq:
        if type(is_kbq) == list:
            if not is_kbq[0]:
                continue

        answers.append(i['a'])


print(len(answers))

with open('datasets/kb_answers.txt', 'w') as f:
    for q in answers:
        f.write(q.encode('utf-8') + '\n')



