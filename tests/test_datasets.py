# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.classifier import baidu_classify
from multiprocessing.dummy import Pool as ThreadPool
import json


test_environment.init_environment()


def classify(question_d):
    question = question_d['q']
    answer = question_d['a']
    count = question_d['id']
    is_kbq = baidu_classify(question)
    if is_kbq:
        print(question)

    return {
        'q': question,
        'a': answer,
        'id': count,
        'is_kbq': is_kbq
    }


def main():
    training_data_filename = 'datasets/nlpcc-iccpol-2016.kbqa.training-data'
    testing_data_filename = 'datasets/nlpcc-iccpol-2016.kbqa.testing-data'

    training_data = read_data_file(training_data_filename)
    testing_data = read_data_file(testing_data_filename)

    pool = ThreadPool(4)
    training_flag_data = pool.map(classify, training_data)
    testing_flag_data = pool.map(classify, testing_data)

    with open('datasets/training_data_kbq_0.json', 'w') as f:
        json.dump(training_flag_data, f)

    with open('datasets/testing_data_kbq_0.json', 'w') as f:
        json.dump(testing_flag_data, f)



def read_data_file(filename):
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
                data.append({'q': question,
                             'id': question_count})

            if line[1] == 'a':
                answer = line[line.find('>') + 2:-1]
                data[-1]['a'] = answer

    return data



if __name__ == '__main__':
    main()


