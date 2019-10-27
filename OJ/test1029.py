# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1029.py -*-
# -*- data: 2019-10-26 -*-

num = input()
num = int(num)
while(num != 0):
    num = num - 1
    number = input()
    number = int(number)
    if (number/2==0):
        print(int((number+1)*2))
    else:
        print(int(number*((number+1)/2)))