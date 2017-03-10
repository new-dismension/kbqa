# coding:utf-8


from __future__ import print_function
import json


with open('datasets/all_cqa_data_kbq_0.json', 'r') as f:
    data = json.load(f)


with open('datasets/cqa_kb_questions.txt', 'w') as f:
    for i in data:
        is_kbq = i['is_kbq']
        if type(is_kbq) == list:
            if is_kbq[0]:
                f.write(i['q'].encode('utf-8') + '\n')
        elif is_kbq:
                f.write(i['q'].encode('utf-8') + '\n')

