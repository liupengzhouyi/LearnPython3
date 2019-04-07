#!usr/bin/python3




list = [1, 2, 3, 4, 5]

print (list[::-1])

# 原理：list的切片有三个参数：起点，终点，步长

# list[::-1]
# 相当于起点是最后第一个，
# 终点是第一个，
# 然后一次减少一个

print(list[3:1:-1])

# [4, 3]



list_a = [1, 2, 3, 4, 5]
list_a.reverse()

for em in list_a:
    print(em)
