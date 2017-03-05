# coding:utf-8


import requests


USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' \
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87' \
             ' Mobile Safari/537.36'
HEADERS = {'User-Agent': USER_AGENT}


def get(url, params):
    r = requests.get(url, params=params, headers=HEADERS)
    return r.text

