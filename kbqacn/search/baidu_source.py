# coding:utf-8


from __future__ import print_function
import kbqacn.common.spider as spider
from kbqacn.common.exception import BaiduSpiderVerifiedError
import time


def search(sentence):
    r = spider.get('https://www.baidu.com/s?wd=%s' % sentence, None)
    html = r.text
    url = r.url

    if url.find('verify.baidu.com') > 0:
        return ban_search(sentence, 0)

    return html


def ban_search(sentence, count):
    r = spider.get('https://www.baidu.com/s?wd=%s' % sentence, None)
    html = r.text
    url = r.url

    if url.find('verify.baidu.com') > 0:
        print('sleep: ' + sentence)
        if count > 20:
            raise(BaiduSpiderVerifiedError('Need to be verified!'))
        else:
            time.sleep(2)
            return ban_search(sentence, count + 1)

    return html

