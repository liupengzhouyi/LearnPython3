#!/usr/bin/python3.7
# -*- coding:UTF-8 -*-
import pickle

from What_is_Pickle.Student import Student

f = open('File/text.txt', 'rb')

s = pickle.load(f)

f.close()

s.print()



