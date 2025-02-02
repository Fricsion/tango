#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json

words = pd.read_csv("sample.csv")
rows = words['word']
columns = words.columns

words_list = []
data_list = []

# 各列に対する処理
for column in columns[1:]:
    data_list.append([column, ''])

# 各行に対する処理
for row in rows:
    words_list.append([row, dict(data_list)])

data_hash = dict(words_list)

print(data_hash)


for i in data_hash:
    for j in columns[1:]:
        print(data_hash[i][j])

words_json = []

fileToWrite = open("output.json", 'w')

json.dump(words_json, fileToWrite, indent=4)

