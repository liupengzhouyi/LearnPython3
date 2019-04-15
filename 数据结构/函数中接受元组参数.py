#!/usr/bin/python3.7
# -*- coding：UTF-8 -*-

def paly(*args):
    '这是一个接受元组的函数'
    total = 0
    for i in args:
        print(i)
        #total = total + i
    return total


# 这是一个元组
tupleDome01 = (1, 2, 3, 6, 4)

# 对元组进行遍历
for i in tupleDome01:
    print(i)

# 把元组当作参数操作
# 函数的功能：接受一个元组进行遍历
# 预期输出：元组内的各个元素
paly(tupleDome01)


# 如何遍历元组？





