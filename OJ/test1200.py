# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1200.py -*-
# -*- data: 2019-10-26 -*-

numbers = ['LING', 'YI', 'ER', 'SAN', 'SI', 'WU', 'LIU', 'QI', 'BA', 'JIU', 'SHI']
try:
    while True:
        number = input()
        number = int(number)
        if(number > 99):
            print("CUO LE")
        elif(number < 0):
            print("CUO LE")
        elif(number in [20, 30, 40, 50, 60, 70, 80, 90]):
            print(numbers[int(number/10)] + " " + numbers[10])
        elif(number in [11, 12, 13, 14, 15, 16, 17, 18, 19]):
            print("SHI " + numbers[int(number%10)])
        elif(number == 10):
            print("SHI")
        else:
            if (number < 10):
                print(numbers[int(number)])
            else:
                print(numbers[int(number/10)] + " " + numbers[10] + " " + numbers[int(number%10)])
except EOFError:
    pass