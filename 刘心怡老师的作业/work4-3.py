# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work4-1.py -*-
# -*- data: 2019-11-04 -*-
from math import sqrt

# a, b, c = map(int, input().split())

a = int(input())
b = int(input())
c = int(input())

key = -1
if a+b <= c:
    key = 0
elif b+c <= a:
    key = 0
elif a+c <= b:
    key = 0
elif a == 0 or b == 0 or c == 0:
    key = 0
else:
    key = 1
if key == 0:
    print("无法构成三角形")
else:
    cc = a + b + c
    ccc = cc / 1.0
    p = ccc/2.0
    ss = sqrt(p*(p-a)*(p-b)*(p-c))
    print("C=" + str(ccc) + " S=" + str(ss))