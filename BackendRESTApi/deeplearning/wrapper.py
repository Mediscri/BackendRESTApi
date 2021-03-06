# -*- coding:utf-8 -*-
import json
import os

from konlpy.tag import Twitter
from sklearn.externals import joblib


def pos_tagging_with_stem(text):
    text_pos = twitter.pos(text, norm=False, stem=True)
    return ' '.join([token for token, pos in text_pos
                        if pos not in ['Punctuation']])


twitter = Twitter()


class Classifier:
    def __init__(self, pipe_file_name='/pipe-svm.sav', level_file_name='/levels.sav'):
        # Importing a module does not change your working directory -> needed
        # to be set in docker environment
        base_path = os.path.dirname(os.path.realpath(__file__))

        self.pipe = joblib.load(base_path+pipe_file_name)
        self.levels = joblib.load(base_path+level_file_name)

    def inference(self, text):
        values = self.pipe.predict_proba([pos_tagging_with_stem(text)])[0]
        top_score_map = sorted([(self.levels[i], values[i]) for i in range(len(values)) if values[i] > 0.12],
                               key=lambda x: -x[1])
        deep_outputs = []
        for cat, prob in top_score_map:
            deep_outputs.append({'category': cat, 'accuracy': prob})
        json_dict = {'deep_output': deep_outputs, 'raw_sentence': text}
        return json.dumps(json_dict)
