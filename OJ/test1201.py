# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1200.py -*-
# -*- data: 2019-10-26 -*-

try:
    while True:
        number = input()
        number = int(number)
        if(number == 1):
            print("NO")
        elif(number == 2):
            print("YES")
        elif(number == 3):
            print("NO")
        else:
            print("YES")
except EOFError:
    pass