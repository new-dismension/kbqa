# coding:utf-8


from __future__ import print_function
import kbqacn.common.spider as spider


def search(sentence):
    html = spider.get('http://www.baidu.com/s?wd=%s' % sentence, None)
    return html


