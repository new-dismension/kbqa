# coding:utf-8



from __future__ import print_function
import json
import os



resources_path = os.path.split(os.path.realpath(__file__))[0]


question_sparql_templates = None

with open(resources_path + '/question_sparql_templates.json', 'r') as f:
    question_sparql_templates = json.load(f)

