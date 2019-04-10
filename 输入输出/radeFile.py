#!/usr/bin/python3.7
# -*- coding:UTF-8 -*-


f = open('File/text.txt')

while True:
    line = f.readline()

    if (line) == 0:
        break

    print(line, end='')

f.close()






