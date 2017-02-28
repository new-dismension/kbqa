# coding:utf-8



from __future__ import print_function
#import thulac
import kbqacn.resources as resources
import jieba


model_path = None
user_dict = None
T2S = False
seg_only = False
filt = False


#thu = thulac.thulac(user_dict=user_dict,
#                    model_path=model_path,
#                    T2S=T2S, seg_only=seg_only,
#                    filt=filt)


def word_parse(sentence):
#    words = thu.cut(sentence)
    words = jieba.cut(sentence)
    return words


def question_sparql_template_parse(sentence):
    for (templates, _) in resources.question_sparql_templates:
        pass



