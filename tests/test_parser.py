# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.parser import question_sparql_template_parse
from kbqacn.parser import word_parse


test_environment.init_environment()


def test_word_parse():
    words = word_parse('Python是一种面向对象、解释型的计算机程序语言')
    print(' '.join(words))
#    for (word, tag) in words:
#        print(word, tag)


def test_question_sparql_template_parse():
    question_sparql_template_parse('百度的创始人是谁')


def test():
    test_word_parse()


if __name__ == '__main__':
    test()
