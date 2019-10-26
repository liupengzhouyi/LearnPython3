# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work3-1.py -*-
# -*- data: 2019-10-26 -*-

number1 = input()
number = str(number1)
value = 0
i = 0
while(value != 1):
    i = i + 1
    for temp in number:
        pp = int(temp)*int(temp)
        value = value + pp
    if (value != 1):
        number = str(value)
        value = 0
        if (i == 1000):
            print("False")
            break
    else:
        print("True")

