#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = 50

def func():
    global x    # 告诉解释器，我是全局变量
    # 在不使用global语句的情况下，
    # 不可能为一个不再函数内部的变量赋值
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value od x is', x)

