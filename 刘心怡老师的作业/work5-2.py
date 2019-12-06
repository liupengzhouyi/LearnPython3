# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work5-2.py -*-
# -*- data: 2019-12-06 -*-

string = str(input())
dictA = {}
for item in string:
    if item in dictA:
        dictA[item] = dictA[item] + 1
    else:
        dictA[item] = 1
print(dictA)


