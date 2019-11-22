# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1061.py -*-
# -*- data: 2019-11-22 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1061

n = int(input())
list = []

while n > 0:
    str1 = str(input())
    list.append(str1)
    n = n - 1

list.sort()

for item in list:
    print(item)
