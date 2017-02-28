# coding:utf-8

from __future__ import print_function
import test_environment
from kbqa.parser import word_parse

test_environment.init_environment()

def test_word_parse():
    words = word_parse('Python是一种面向对象、解释型的计算机程序语言')
    for (word, tag) in words:
        print(word, tag)

def test():
    test_word_parse()


if __name__ == '__main__':
    test()
