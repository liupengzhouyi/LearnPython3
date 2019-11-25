# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1500.py -*-
# -*- data: 2019-11-19 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1500


dic = {}

i=0
while(i < 26):
    dic[chr(ord('a')+i)] = 0
    i = i + 1

try:
    key = True
    while True:
        tempStr = str(input())
        for item in tempStr:
            if item == '#':
                for key,value in dic.items():
                    print(key,value)
                key = False
                break
            else:
                if item in dic:
                    dic[item] = int(dic[item]) + 1
        if key == False:
            break
except EOFError:
    pass
