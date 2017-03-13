# coding:utf-8


from __future__ import print_function
import gzip
import json


infile = gzip.GzipFile('20170306.json.gz', 'r')
infile.readline()


with open('item_dictronary.txt', 'w') as f:
    count = 0

    for line in infile:
        count = count + 1
        entity = line[:-2]

        try:
            entity = json.loads(entity)
        except Exception:
            print('end!')
            break

        labels = entity['labels']
        aliases = entity['aliases']

        name = None

        if 'zh-cn' in labels:
            name = labels['zh-cn']['value']
        elif 'zh-hans' in labels:
            name = labels['zh-hans']['value']

        aliases_zh = None
        if 'zh' in aliases:
            aliases_zh = aliases['zh']
            for zh_aliase in aliases_zh:
                aliase_zh_value = zh_aliase['value']
                f.write(aliase_zh_value.encode('utf-8') + '\n')

        if name:
            if count % 1000 == 0:
                print(count, name)
            f.write(name.encode('utf-8') + '\n')
