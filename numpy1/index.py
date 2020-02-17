import numpy

a = numpy.arange(10)
print(a)
#  索引从2开始7结束，间隔=2
s = slice(2,7,2)
print(a[s])

a = numpy.arange(100)
print(a)
#  索引从2开始7结束，间隔=2
s = slice(2,7,2)
print(a[s])

print(a[2:7:2])
print(a[5:1:-1])

a = numpy.arange(100)
a.shape = (10, 10)
print(a)

#  显示第几行到第几行
print(a[2:4])

# 显示某一列
print(a[..., 5])

# 显示某一行
print(a[5, ...])

# 显示第六列第5个元素之后的信息
print(a[5:, 6])


