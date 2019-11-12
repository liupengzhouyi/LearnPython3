# -*- coding: UTF-8 -*-
# -*- author: liupeng -*-
# -*- fileName: test1392.py -*-
# -*- data: 2019-11-12 -*-
# -*- problem url: https://imustacm.cn/problem/getProblem/1392

# i = 0
# temp = 1
# numberList = []
# while(i<=20):
#     i = i + 1
#     temp = temp * i
#     numberList.append(temp)
# print(numberList)

numberList = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000, 51090942171709440000]
n = int(input())
i = 0
sum = 0
while(i < n):
    sum = sum + numberList[i]
    i = i + 1
print(sum)
