# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.classifier import baidu_classify
from multiprocessing.dummy import Pool as ThreadPool
from kbqacn.common.exception import BaiduSpiderVerifiedError
import json
import threading


test_environment.init_environment()


mutex = threading.Lock()

temp_data = {
    'train': {},
    'test': {},
}

spider_count = 0

def temp_save(q, a, q_id, is_kbq, tag):
    global spider_count

    mutex.acquire()

    temp_data[tag][q_id] = {
        'q': q,
        'a': a,
        'is_kbq': is_kbq
    }

    if spider_count % 50 == 0:
        with open('datasets/question_data_kbq_0.json', 'w') as f:
            json.dump(temp_data, f)

    spider_count = spider_count + 1

    mutex.release()


def classify(question_d):
    question = question_d['q']
    answer = question_d['a']
    q_id = question_d['id']
    tag = question_d['tag']

    mutex.acquire()
    if q_id in temp_data[tag]:
        is_kbq = temp_data[tag][q_id]['is_kbq'],
        if is_kbq:
            print('Hit: ' + question)

        res = {
            'q': question,
            'a': answer,
            'id': q_id,
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
        print(str(q_id) + ': ' + question)

    temp_save(question, answer, q_id, is_kbq, tag)

    return {
        'q': question,
        'a': answer,
        'id': q_id,
        'is_kbq': is_kbq
    }


def main():
    global temp_data

    with open('datasets/question_data_kbq_0.json', 'r') as f:
        temp_data = json.load(f)

    training_data_filename = 'datasets/nlpcc-iccpol-2016.kbqa.training-data'
    testing_data_filename = 'datasets/nlpcc-iccpol-2016.kbqa.testing-data'

    training_data = read_data_file(training_data_filename, 'train')
    testing_data = read_data_file(testing_data_filename, 'test')

    pool = ThreadPool(10)
    training_flag_data = pool.map(classify, training_data)
    testing_flag_data = pool.map(classify, testing_data)

    with open('datasets/training_data_kbq_0.json', 'w') as f:
        json.dump(training_flag_data, f)

    with open('datasets/testing_data_kbq_0.json', 'w') as f:
        json.dump(testing_flag_data, f)



def read_data_file(filename, tag):
    question_count = 0
    data = []
    with open(filename, 'r') as training_f:
        f = training_f
        for line in f:
            if line[0] == '=':
                continue

            if line[1] == 'q':
                question_count = question_count + 1
                question = line[line.find('>') + 2:-1]
                data.append({
                    'q': question,
                    'id': str(question_count),
                    'tag': tag,
                })

            if line[1] == 'a':
                answer = line[line.find('>') + 2:-1]
                data[-1]['a'] = answer

    return data



if __name__ == '__main__':
    main()


