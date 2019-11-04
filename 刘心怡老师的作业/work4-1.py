# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work4-1.py -*-
# -*- data: 2019-11-04 -*-

number = int(input())
if number <= 10:
    print(number*0.32)
elif number <= 20 and number > 10:
    number = number - 10
    print(3.2 + number*0.64)
else:
    number = number - 20
    print(3.2 + 6.4 + number*0.96)