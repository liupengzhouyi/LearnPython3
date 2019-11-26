# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1053.py -*-
# -*- data: 2019-11-26 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1053

def Fb(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return Fb(n-1) + Fb(n-2)

n = int(input())
while n > 0:
    print(Fb(int(input())))
    n -= 1
