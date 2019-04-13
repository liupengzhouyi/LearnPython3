#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-



print("Hello World!")



try:
    text = input("Enter something --->")
except EOFError:
    print("字符输入停止！")
except KeyboardInterrupt:
    print("你的输入错误！")
else:
    print("你的输入信息{}".format(text))




