# coding:utf-8


from __future__ import print_function
import test_environment
import kbqacn.common.spider as spider


test_environment.init_environment()


def test_get():
    print(len(spider.get('http://www.baidu.com/s?wd=特朗普妻子&nojs=1', None)))


def test():
    print(spider.USER_AGENT)
    test_get()


if __name__ == '__main__':
    test()

