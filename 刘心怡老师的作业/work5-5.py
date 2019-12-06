# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work5-5.py -*-
# -*- data: 2019-12-06 -*-

def newList(listA):
    listC = []
    sum = 0
    for index in range(0, len(listA)):
        if listA[index] == 0:
            sum = sum + 1
            continue
        else:
            listC.append(listA[index])
    i = 0
    while i < sum:
        listC.append(0)
        i = i + 1
    return listC

listA = list(eval(input()))
listB = newList(listA)
print(listB)

