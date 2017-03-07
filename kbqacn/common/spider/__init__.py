# coding:utf-8


import requests
import random


USER_AGENT_MOBILE_CHROME = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) ' \
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87' \
                    ' Mobile Safari/537.36'

USER_AGENT_PC_CHROME = 'Mozilla/5.0 (Windows NT 10.0; WOW64)' \
                ' AppleWebKit/537.36 (KHTML, like Gecko)' \
                ' Chrome/56.0.2924.87 Safari/537.36'

USER_AGENT_PC_FIREFOX = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'


headers_chrome = {'User-Agent': USER_AGENT_PC_CHROME}
headers_firefox = {'User-Agent': USER_AGENT_PC_FIREFOX}


def get(url, params=None):
    headers = headers_chrome if random.random() > 0.5 else headers_firefox
    r = requests.get(url, params=params, headers=headers)
    return r

