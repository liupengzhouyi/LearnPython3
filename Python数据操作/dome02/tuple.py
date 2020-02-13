
temp = (1, 2, 3, 4)

print(type(temp))

print(temp)

temp1 = ()

print(type(temp1))

temp2 = (1, [2, 3, 4], 3)

# 可变
temp2[1][2] = 999
# 不可变
# temp2[1] = [9, 9, 9]

for i in temp2:
    print(i)
