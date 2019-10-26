# -*- coding: UTF-8 -*-
# fileName：work1-1.py
# author: liupeng
# data : 2019-10-26
from _decimal import Decimal

str1 = input("")

strType = ""

strValue = ""

# 一个方法：分类字符串
def isChar(char):
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        return 1
    else:
        return 0

for char in str1:
    if (isChar(char) == 0):
        strType = strType + char
    else:
        strValue = strValue + char

number = float(strValue)

if (strType in ["C"]):
    value = number*1.8+32
    value = Decimal(value).quantize(Decimal('0.00'))
    print("F" + str(value))
else:
    value = (number-32)/1.8
    value = Decimal(value).quantize(Decimal('0.00'))
    print("C" + str(value))
