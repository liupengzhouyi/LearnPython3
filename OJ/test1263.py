# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1263.py -*-
# -*- data: 2019-11-05 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1263

def getNumber(number):
    sum = number
    while sum > 9:
        tempNumber = 0
        while number > 9:
            temp = number % 10
            number = int(number/10)
            tempNumber = tempNumber + temp
        tempNumber = tempNumber + number
        if tempNumber > 9:
            number = tempNumber
        else:
            sum = tempNumber
    return sum

n = int(input())
while n > 0:
    n = n - 1
    yourStr = str(input())
    newStr = ""
    list = [0,0,0,0,0,0]
    index = 0
    for ch in yourStr:
        index = index % 6
        list[index] = list[index] + ord(ch)
        index = index + 1
    for l in list:
        newStr = newStr + str(getNumber(l))
    print(newStr)

