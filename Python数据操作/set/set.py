

s = set([1, 5, 3, 6, 5])

print(s)

# add
s.add(7)
print(s)

# delete || remove
s.remove(5)
print(s)


s1 = set([1,10,3,12,5])
s2 = set([12,2,7,8,9])

# 交集
s3 = s1 | s2
print('s3: ', s3)

# 并集
s4 = s2 & s1
print('s4:', s4)

# is in set
if 1 not in s3:
    print('n')
else:
    print('y')

# set([()])
s5 = set([123, 124, 12, 23, (11,2,3)])
print(s5)

# set((()))
s7 = set((123,(11,2,(11,1,3),3,4), 124, 12, 23, (11,2,3), (11,2,3)))
print(s7)

# update = remove + add
