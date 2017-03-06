# coding:utf-8


from bs4 import BeautifulSoup
from kbqacn.search import baidu_search


def classify(sen):
    html = baidu_search(sen)
    soup = BeautifulSoup(html)
    return len(soup.select('.result-op.c-container .c-border')) > 0

