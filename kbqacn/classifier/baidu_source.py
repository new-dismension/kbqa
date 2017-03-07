# coding:utf-8


from bs4 import BeautifulSoup
from kbqacn.search import baidu_search


def classify(sen):
    html = baidu_search(sen)
    soup = BeautifulSoup(html)

    if len(soup.select('.op_exactqa_main')) == 0:
        return False

    divs = soup.select('.result-op.c-container')

    if len(divs) > 0:
        for div in divs:
            if div['id'] == '1':
                return True

    return False

