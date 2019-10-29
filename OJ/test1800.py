# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1200.py -*-
# -*- data: 2019-10-26 -*-

strA = input()
strA = str(strA)
strB = input()
strB = str(strB)
i = 0
index = 0
while(index != -1):
    i = i + 1
    index = strB.find(strA)
    longth = len(strA)
    newStr = strB[0:index] + strB[int(index + longth):len(strB)]
    # print(newStr + '\n')
    strB = newStr
print(i-1)

