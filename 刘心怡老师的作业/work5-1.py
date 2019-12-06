# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work5-1.py -*-
# -*- data: 2019-12-06 -*-

def remooveList(listA, listB):
    listC = []
    for index in range(0, len(listA)):
        if listA[index] in listB:
            continue
        else:
            listC.append(listA[index])
    return listC


listA = list(eval(input()))
listB = []
listB.append(int(input()))
listC = remooveList(listA, listB)
print(listC)

