#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-



print("Hello World!")



try:
    text = input("Enter something --->")
except EOFError:
    print("字符输入停止！")
except KeyboardInterrupt:
    print("")
else:
    print()




