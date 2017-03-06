# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.classifier import baidu_classify


test_environment.init_environment()


def test_baidu_classify():
    print(baidu_classify('特朗普妻子'))
    print(baidu_classify('search'))
    print(baidu_classify('kdafjadaf'))



def test():
    test_baidu_classify()


if __name__ == '__main__':
    test()

