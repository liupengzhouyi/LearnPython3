#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-

class Paly01:
    '这是一个类的构建，母的是为了学习__init__()方法。'
    def __init__(self, name, a):
        self.name = name
        self.a = a

    def say_hi(self):
        print('My name is', self.name)


# 常见一个类对象
p = Paly01('liupeng', 2)

# 掉哟类对象的方法
p.say_hi()

