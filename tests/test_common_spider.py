# coding:utf-8


from __future__ import print_function
import test_environment
import kbqacn.common.spider as spider


test_environment.init_environment()


def test_get():
    with open('test.html', 'w') as f:
        f.write(spider.get('http://www.baidu.com/s?wd=特朗普妻子&nojs=1', None).encode('utf-8'))
    print(len(spider.get('http://www.baidu.com/s?wd=特朗普妻子&nojs=1', None)))


def test():
    print(spider.USER_AGENT)
    test_get()


if __name__ == '__main__':
    test()

