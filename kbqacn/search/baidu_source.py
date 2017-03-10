# coding:utf-8


from __future__ import print_function
import kbqacn.common.spider as spider
from kbqacn.common.exception import BaiduSpiderVerifiedError
from bs4 import BeautifulSoup
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


def kb_search(sentence):
    html = search(sentence)
    soup = BeautifulSoup(html)

    answer_div = soup.select('.op_exactqa_s_answer')

    if len(answer_div) == 0:
        return None

    prop_div = soup.select('.op_exactqa_s_prop')

    answer = answer_div[0].string.replace(' ', '').replace('\n', '')
    entity = prop_div[0].a.string
    relation = prop_div[0].contents[-1].replace('\n', '').replace(' ', '')[:-1]

    return {
        'answer': answer,
        'entity': entity,
        'relation': relation,
    }

