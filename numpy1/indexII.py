import numpy

x = numpy.arange(6)
x.shape = (3,2)
print(x)

# [[0 1]
#  [2 3]
#  [4 5]]

y = x[[1, 2],[1, 0]]
print(y)
# [3 4]


x = numpy.arange(9)
x.shape = (3, 3)
print(x)

# 切行，获取元素
y = x[1:3, [1, 2]]
print(y)

#  获取列
z = x[..., 2:]
print(z)

x = numpy.arange(9)
x.shape = (3, 3)
print(x[x>5])

x = numpy.arange(60).reshape(6, 10)
print(x)
# 获取第1，2，3行
print(x[[1,2,3]])

# 获取倒数第1，2，3行
print(x[[-1,-2,-3]])

x = numpy.arange(9)
x.shape = (3, 3)
print(x[numpy.ix_([2, 1], [1, 2])])

# for i in numpy.nditer(x):
#      print(i)

x = numpy.arange(12)
x.shape = (3, 4)
print(x)

# 修改数据形状
x = x.reshape((4, 3))
print(x)




