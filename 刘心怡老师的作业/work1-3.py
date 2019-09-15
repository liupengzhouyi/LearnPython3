# -*- coding: UTF-8 -*-
# 文件名：work1-3.py

# 一个方法：分类字符串
def isChar(char):
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return 1
    else:
        return 0

# 一个方法，计算汇率
def exchangeRate(type, money):
    if (type == "$") :
        money = float(money) * 6.78
    elif (type == "￥") :
        money = float(number) / 6.78
    elif (type == "USD") :
        money = float(money) * 6.78
    elif (type == "RMB"):
        money = float(number) / 6.78
    return money

def addType(type, money):
    if (type == "$") :
        money = "￥" + money
    elif (type == "￥") :
        money = "$" + money
    elif (type == "USD") :
        money = "RMB" + money
    elif (type == "RMB"):
        money = "USD" + money
    return print(money)

# 用户输入
money = input("")
# 数值
number = ""
# 类型
type = ""
# 分离
for char in money :
    if (isChar(char) == 1) :
        number = number + char
    else :
        type = type + char
# 去空格
type.strip()
# 去空格
money.strip()
# 计算
newMoney = ("{:.2f}".format(exchangeRate(type, number)))
# 输出
addType(type, newMoney)








