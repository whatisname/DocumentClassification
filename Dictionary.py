# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 01:27:27 2019

@author: XX
Reference
---------
https://github.com/dwyl/english-words
"""

import json
import os, sys

class Dictionary:
    def __init__(self):
        self.english_words = self.load_words()

    def load_words(self):
        try:
            filename = os.path.dirname(sys.argv[0])+"\\"+"words_dictionary.json"
            with open(filename,"r") as enlish_dictionary:
                valid_words = json.load(enlish_dictionary)
                return valid_words
        except Exception as e:
            return str(e)
    
    def lookup(self, word):
        try:
            if self.english_words[word] == 1:
                return True
        except KeyError:
            return False

if __name__ == '__main__':
    dic = Dictionary()
    print(dic.word('fate'))
    print(dic.word('uuuuu'))