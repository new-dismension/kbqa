# coding:utf-8


from __future__ import print_function
import test_environment
import os
from kbqacn.classifier import baidu_classify
from multiprocessing.dummy import Pool as ThreadPool
from kbqacn.common.exception import BaiduSpiderVerifiedError
import json
import threading


test_environment.init_environment()


mutex = threading.Lock()

spider_count = 0

def temp_save(q, is_kbq):
    global spider_count

    mutex.acquire()

    temp_data[q] = is_kbq

    if spider_count % 1000 == 0:
        print('save...')
        with open('datasets/cqa_question_data_kbq_0.json', 'w') as f:
            json.dump(temp_data, f)

    spider_count = spider_count + 1

    mutex.release()


def classify(question):
    mutex.acquire()
    if question in temp_data:
        is_kbq = temp_data[question],
        if is_kbq:
            print('Hit: ' + question)

        res = {
            'q': question,
            'is_kbq': is_kbq,
        }

        mutex.release()
        return res

    mutex.release()

    try:
        is_kbq = baidu_classify(question)
    except BaiduSpiderVerifiedError:
        is_kbq = False

    if is_kbq:
        print(str(spider_count) + ': ' + question)

    temp_save(question, is_kbq)

    return {
        'q': question,
        'is_kbq': is_kbq
    }


def main():
    global temp_data

    with open('datasets/cqa_question_data_kbq_0.json', 'r') as f:
        temp_data = json.load(f)

    all_questions = []

    for filename in os.listdir('datasets/cqa_triple_match'):
        all_questions = all_questions + read_data_file('datasets/cqa_triple_match/' + filename)

    if True:
        pool = ThreadPool(10)
        questions_data = pool.map(classify, all_questions)
    else:
        for q in all_questions:
            classify(q)

    with open('datasets/all_cqa_data_kbq_0.json', 'w') as f:
        json.dump(questions_data, f)


def read_data_file(filename):
    data = []
    data_dic = {}
    with open(filename, 'r') as training_f:
        f = training_f
        for line in f:
            question = line.split(None)[0]
            question = question.decode('utf-8')
            if question not in data_dic:
                data.append(question)
                data_dic[question] = True

    return data


def test():
    for q in read_data_file('datasets/cqa_triple_match/part-00000'):
        print(q)


if __name__ == '__main__':
    main()



