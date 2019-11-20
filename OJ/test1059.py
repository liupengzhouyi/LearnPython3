# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1059.py -*-
# -*- data: 2019-11-19 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1059

n = int(input())

while n > 0:
    n = n - 1
    list1 = []
    sum = 0
    list1 = input().split()
    key = int(input())
    for number in list1:
        if int(number) <= key + 30:
            sum = sum + 1
    print(sum)

