# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1219.py -*-
# -*- data: 2019-10-29 -*-


def paly(gemType, number, key):
    if (gemType not in list): # 没有初始化
        list[gemType] = number
    else:
        list[gemType] = list[gemType] + number
    num = int(list[gemType] / 3)
    number = int(list[gemType] % 3)
    # 设置本场
    list[gemType] = number
    # 预定下一个
    if (gemType + 1 not in list):
        list[gemType + 1] = 0
    # 设置下一个
    list[gemType + 1] = list[gemType + 1] + num
    # 判定下一个
    if (list[gemType + 1] >= 3):
        paly(gemType + 1, 0, 1)

times = int(input())
i = 0
while(times >= 0):
    times = times - 1
    i = i + 1
    typeNumbers = input()
    typeNumbers = int(typeNumbers)
    d = 0
    sum = 0
    list = {}
    while(typeNumbers >= 0):
        typeNumbers = typeNumbers - 1
        gemType, number = map(int, input().split())
        paly(gemType, number, 0)
    for item,value in list.items():
        print(item, value)
        sum = sum + int(value)
    print("Case #" + str(i) + ":")
    print(sum)
    list.clear()

