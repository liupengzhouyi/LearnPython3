# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1097.py -*-
# -*- data: 2019-11-15 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1097

class Node:

    def __init__(self, number, name, index):
        self.number = int(number)
        self.name = name
        self.index = int(index)
        self.value = (100 - self.index) * 1000000000000 + self.number
        # self.value = int(index) * 1000000000 + (100000000 - int(number))

    def show(self):
        print(self.number, self.name, self.index)

n = int(input())
list1 = []
while n > 0:
    list2 = input().split()
    node = Node(list2[0], list2[1], list2[2])
    list1.append(node)
    n = n - 1

list1 = sorted(list1, key = lambda node : node.value)

for item in list1:
    item.show()


