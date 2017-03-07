# coding:utf-8


from __future__ import print_function
import kbqacn.common.spider as spider


def search(sentence):
    r = spider.get('https://www.baidu.com/s?wd=%s' % sentence, None)
    html = r.text
    url = r.url

    if url.find('verify.baidu.com') > 0:
        raise(Exception('Need to be verified!'))

    return html


