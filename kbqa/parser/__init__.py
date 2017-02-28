# coding:utf-8


import thulac


model_path = None
user_dict = None
T2S = False
seg_only = False
filt = False

thu = thulac.thulac(user_dict=user_dict,
                    model_path=model_path,
                    T2S=T2S, seg_only=seg_only,
                    filt=filt)

def word_parse(sentence):
    words = thu.cut(sentence)
    return words



