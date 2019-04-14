#!/usr/bin/python3
# -*- coding:UTF-8 -*-

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter some --> ')
    if (len(text) < 3):
        raise ShortInputException(len(text), 3)

except EOFError:
    print("突然停止！")
except ShortInputException as ex:
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No expcetion was raised')



