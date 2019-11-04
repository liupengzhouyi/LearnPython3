# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: work4-4.py -*-
# -*- data: 2019-11-04 -*-

#条件判断，当输入错误时可重新输入

#数据的接受
a=int(input())
a = a*2-1
#条件判断
if a%2==1:
    b=(a//2)+1
    #图形绘制
    for i in range(1,int(a-1),2):
        print(("*"*i).center(a),'\n')
    for i in range(int(a),0,-2):
        print(("*"*i).center(a),'\n')





