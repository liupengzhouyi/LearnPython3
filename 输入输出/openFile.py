#!/usr/bin/python3.7
# -*- coding:UTF-8 -*-

txt = '''\
    progamming is fun
    when the work iss dome 
    if you wanna make your also fun:
        use Python!
'''

f = open('File/text.txt')

while True:
    line = f.readline()

    if (line) == 0:
        break

    print(line, end='')

f.close()






