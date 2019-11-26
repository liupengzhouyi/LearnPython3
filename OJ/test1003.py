# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1003.py -*-
# -*- data: 2019-11-19 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1003
import math as mh
from decimal import Decimal


# 导入math包
import math


# 定义点的函数
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y
    # 定义直线函数


class Getlen:
    def __init__(self, p1, p2):
        self.x = p1.getx() - p2.getx()
        self.y = p1.gety() - p2.gety()
        # 用math.sqrt（）求平方根
        self.len = math.sqrt((self.x ** 2) + (self.y ** 2))

    # 定义得到直线长度的函数
    def getlen(self):
        return self.len


try:
    while True:
        str1 = input()
        if str1 == "":
            break
        x1, y1, x2, y2 = map(int,str1.split())
        # 设置点p1的坐标为（0,0）
        p1 = Point(x1, y1)
        # 设置点p2的坐标为（3,4）
        p2 = Point(x2, y2)
        # 定义对象
        l = Getlen(p1, p2)
        # 获取两点之间直线的长度
        d = l.getlen()

        # print(Decimal(mh.sqrt(x * x + y * y)).quantize(Decimal("0.00")))
        # print(round(mh.sqrt(x * x + y * y)),2)
        str2 = str(float('%.2f'%float(d)))
        if len(str2) == 4:
            print(str2)
        else:
            print(str2 + '0')
except EOFError:
    pass




