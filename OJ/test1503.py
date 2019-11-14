# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1503.py -*-
# -*- data: 2019-11-12 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1503

class Node:

    def __init__(self, name, index, sum):
        self.name = str(name)
        self.index = int(index)
        self.sum = int(sum)
        self.value = index * 1000000 + (1000 - sum) * 1000 + name

    def say(self):
        return self.name, self.index, self.sum


n, fraction = map(int, input().split())
rList = []

while True:
    try:
        tempList = input().split()
        i = 0
        sum = 0
        index = 0
        name = ''
        for tempStr in tempList:
            i = i + 1
            if i == 1:
                name = tempStr
                continue
            else:
                if '(' in tempStr:
                    tempStr = tempStr[:-1]
                    index = index + 1
                    sum = sum + int(tempStr.split('(')[0]) + fraction * int(tempStr.split('(')[1])
                else:
                    if int(tempStr) > 0:
                        index = index + 1
                        sum = sum + int(tempStr)
        # print(name, index, sum)
        node = Node(str(name), int(index), int(sum))
        rList.append(node)
    except:
        break

rList = sorted(rList,key=lambda node: node.value, reverse=True)


# 对题数排序
rList = sorted(rList,key=lambda node: node.index, reverse=True)


# 对相同题数条件下，分数排序
printList = []
while n >= 0:
    newList = []
    for item in rList:
        if item.index == n:
            newList.append(item)
    newList = sorted(newList, key=lambda node: node.sum)
    for item in newList:
        printList.append(item)
    n = n - 1

# for item in printList:
#     print(item.say())



