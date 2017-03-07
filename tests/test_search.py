# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.search import baidu_search


test_environment.init_environment()


def test_baidu_search():
    print(len(baidu_search('特朗普妻子')))


def test():
    test_baidu_search()


if __name__ == '__main__':
    test()

