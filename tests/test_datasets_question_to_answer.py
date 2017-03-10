# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.search import baidu_kb_search
from multiprocessing.dummy import Pool as ThreadPool
from kbqacn.common.exception import BaiduSpiderVerifiedError
import json
import threading


test_environment.init_environment()


mutex = threading.Lock()

spider_count = 0

def temp_save(q, kb_res):
    global spider_count

    mutex.acquire()

    temp_data[q] = kb_res

    if spider_count % 1000 == 0:
        print('save...')
        with open('datasets/all_cqa_question_to_kb_data.json', 'w') as f:
            json.dump(temp_data, f)

    spider_count = spider_count + 1

    mutex.release()


def kb_answer(question):
    mutex.acquire()
    if question in temp_data:
        kb_res = temp_data[question]
        print('Hit: ' + question)

        if kb_res is not None:
            res = {
                'question': question,
                'answer': kb_res['answer'],
                'entity': kb_res['entity'],
                'relation': kb_res['relation'],
            }
        else:
            res = None

        mutex.release()
        return res

    mutex.release()

    try:
        kb_res = baidu_kb_search(question)
    except BaiduSpiderVerifiedError:
        kb_res = None

    if kb_res is not None:
        print(str(spider_count) + ': ' + question)
        print('entity: ', kb_res['entity'])
        print('relation: ', kb_res['relation'])
        print('qnswer: ', kb_res['answer'])

    temp_save(question, kb_res)

    return kb_res


def main():
    global temp_data

    with open('datasets/all_cqa_question_to_kb_data.json', 'r') as f:
        temp_data = json.load(f)

    all_questions = read_data_file('datasets/cqa_kb_questions.txt')

    if True:
        pool = ThreadPool(10)
        questions_data = pool.map(kb_answer, all_questions)
    else:
        for q in all_questions:
            kb_answer(q)

    with open('datasets/all_cqa_kb_data_e_r_e.json', 'w') as f:
        json.dump(questions_data, f)


def read_data_file(filename):
    data = []
    with open(filename, 'r') as training_f:
        f = training_f
        for line in f:
            question = line[:-1]
            question = question.decode('utf-8')
            data.append(question)

    return data


if __name__ == '__main__':
    main()



