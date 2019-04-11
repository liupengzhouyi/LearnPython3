#!/usr/bin/python3.7
# -*- coding:UTF-8 -*-

txt = '''\
    progamming is fun
    when the work iss dome 
    if you wanna make your also fun:
        use Python!
'''
# 打开文件
f = open('File/text.txt')

while True:
    line = f.readline()
    # 如果都到一行，而且这一行的长度为0
    if (line) == 0:
        break
    # 打印这一行的内容到屏幕上
    # 为什么需要有一个 end='' ,这是因为我们需要在这一样最后输出
    # 但是，我们的在读取的过程中已经有了一个换行符
    # 所以我们什么也不写入
    print(line, end='')

# 关闭文件
f.close()






