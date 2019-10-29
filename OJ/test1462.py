# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1200.py -*-
# -*- data: 2019-10-26 -*-

str1 = input()
str1 = str(str1)

list = [{}]

for ch in str1:
    print(ch)
    key = 0
    for item in list:
        if(item[0] == ch):
            item[1] = item[1] + 1
            key = 1
            break
    if (key == 1):
        list.append({ch:1})

print(list)