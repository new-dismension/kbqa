# coding:utf-8


import requests


USER_AGENT_MOBILE = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' \
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87' \
                    ' Mobile Safari/537.36'

USER_AGENT_PC = 'Mozilla/5.0 (Windows NT 10.0; WOW64)' \
                ' AppleWebKit/537.36 (KHTML, like Gecko)' \
                ' Chrome/56.0.2924.87 Safari/537.36'


HEADERS = {'User-Agent': USER_AGENT_PC}


def get(url, params=None):
    r = requests.get(url, params=params, headers=HEADERS)
    return r.text

