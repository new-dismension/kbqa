# coding:utf-8


from __future__ import print_function
import test_environment
from kbqacn.search import baidu_search
from kbqacn.search import baidu_kb_search


test_environment.init_environment()


def test_baidu_search():
    print(len(baidu_search('特朗普妻子')))


def test_kb_search():
    a = baidu_kb_search('李宁是哪里人？')
    for k, v in a.items():
        print(k, v)

#    print(baidu_kb_search('求好看的小说？'))

#    print(baidu_kb_search('xanxus的声优？'))
    print(baidu_kb_search('红高粱的作者是谁？'))

def test():
#    test_baidu_search()
    test_kb_search()


if __name__ == '__main__':
    test()

