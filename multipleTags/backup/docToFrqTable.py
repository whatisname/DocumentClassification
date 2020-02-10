# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:58:20 2020

@author: XX
"""

filepath = 'forum.data'
documents = []

print('reading file ...')
with open(filepath, encoding='utf-8') as fp:
    line = fp.readline()
    while(line):
        documents.append(line)
        line = fp.readline()

word_list = dict() # 'word': position
doc_word_count = []

for line in documents:
    for word in line.split():
            
        doc_word_count.append()
    
