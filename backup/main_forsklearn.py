# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:51:07 2020

@author: XX
"""
import time
import math
import plot
import numpy as np
#from PorterStemmer import PorterStemmer
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
 
stop_words = stopwords.words('english')
filepath = 'forum.data'
raw_documents = [] # save all the original messages
documents = [] # cleaned documents

# 1. reading file
print('reading file ...')
with open(filepath, encoding='utf-8') as fp:
    line = fp.readline()
    while(line):
        raw_documents.append(line)
        line = fp.readline()

# 2. normalization
print('normalizing ...')
for line in raw_documents:
    filtered_word = [word for word in line.split(' ') if word not in stop_words]
    documents.append(filtered_word)
# generate proper dataset for sklearn
wordlist = dict()
targets = [] # labels
freq_dict = []

for line in documents:
    targets.append(line[1]) # add first word into targets to save the labels
    line = line[2:len(line)] # remove the fist word
    d_c = dict()
    for word in line:
        if word not in wordlist:
            wordlist[word] = 0
        if word in d_c:
            d_c[word] += 1
        else:
            d_c[word] = 1
    freq_dict.append(d_c)

print(len(wordlist))
print(len(targets))
print(len(freq_dict))

wordlist = list(wordlist.keys())
vocab = np.zeros(shape=(len(freq_dict), len(wordlist)), dtype=int )
for index1, f_dict in enumerate(freq_dict):
    for index2, word in enumerate(wordlist):
        if word in f_dict:
            vocab[index1][index2] = f_dict[word]
print(vocab)


# 3. train
print('training ...')

# 4. validate

# 5. plot
    

