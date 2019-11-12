# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1297.py -*-
# -*- data: 2019-11-12 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1297

while 1:
    bottleNumber = int(input())
    if bottleNumber == 0:
        break
    if (bottleNumber < 5):
        print(1)
    else:
        print(int(bottleNumber/2))
