#!/usr/bin.python3.7
# -*- coding: UTF-8 -*-

class robot:
    """
    这是一个机器人类
    这个机器人会自己做饭，和洗衣服
    但是没有名字，只有编号和年龄
    key1 = true ,表示会自己洗衣服
    key2 = true ,表示会自己做饭
    """
    robotNumbers = 0

    def __init__(self, number, age, key1, key2):
        self.number = number
        self.age = age
        self.key1 = key1
        self.key2 = key2
        robot.robotNumbers = robot.robotNumbers + 1

    def cooked(self):
        if self.key2:
            print('我会做饭！')
        else:
            print('我不会做饭')

    def wash(self):
        if self.key1:
            print('我会洗衣服')
        else:
            print('我不会洗衣服')

    def print(self):
        print('------------------------------')
        print('My number is', self.number)
        print('My age is', self.age)
        self.cooked()
        self.wash()
        print('------------------------------')




robot01 = robot('001', 12, True, False)

robot02 = robot('002', 14, True, True)

robot03 = robot('003', 15, True, False)

robot04 = robot('004', 11, True, True)

robot05 = robot('005', 15, False, False)

robot06 = robot('006', 13, True, False)

list = [robot01, robot02, robot03, robot04, robot05, robot06]


for i in list:
    i.print()

print('机器人总数：', robot.robotNumbers)

print(robot.__doc__)

