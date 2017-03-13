# coding:utf-8


from __future__ import print_function
import json


data = None
with open('datasets/all_cqa_kb_data_e_r_e.json', 'r') as f:
    data = json.load(f)


data_without_none = []
for i in data:
    if i is not None:
        data_without_none.append(i)


print(len(data_without_none))


with open('datasets/all_cqa_kb_data_q_e_r_q.json', 'w') as f:
    json.dump(data_without_none, f)


count = 0
with open('datasets/all_cqa_kb_data_q_e_r_q.txt', 'w') as f:
    for i in data_without_none:
        count = count + 1
        f.write(str(count) + '.\n')
        f.write('question: ' + i['question'].encode('utf-8') + '\n')
        f.write('answer: ' + i['answer'].encode('utf-8') + '\n')
        f.write('entity: ' + i['entity'].encode('utf-8') + '\n')
        f.write('relation: ' + i['relation'].encode('utf-8') + '\n')
        f.write('==================================================\n')

