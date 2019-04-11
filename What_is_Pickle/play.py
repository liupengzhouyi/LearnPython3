#!/usr/bin/python3.7
# -*- coding:UTF-8 -*-
import pickle

from What_is_Pickle.Student import Student

s = Student('liupeng')

f = open('File/text.txt', 'wb')

pickle.dump(s, f)

f.close()

del s



