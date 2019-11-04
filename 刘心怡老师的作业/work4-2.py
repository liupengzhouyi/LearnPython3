# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work4-1.py -*-
# -*- data: 2019-11-04 -*-

number = int(input())
n = int(input())
index = n
sum = 0
i = 0
while(i<index):
    temp = number*n
    sum = sum + temp
    number = number * 10
    n = n - 1
    i = i + 1
print(sum)