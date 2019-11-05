# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1271.py -*-
# -*- data: 2019-11-05 -*-
# -*- problem url: https://imustacm.cn/contest/getProblem/1271/0
import math

n = int(input())
while n > 0:
    n = n - 1
    binaryString = str(input())
    index = 0
    sum = 0
    l = list(binaryString)
    while len(l) > 0:
        if l.pop() == '1':
            sum = sum + math.pow(2, index)
        index = index + 1
    print(int(sum))





