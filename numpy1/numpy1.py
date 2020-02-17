import numpy

a = numpy.array([[1,2,3],[4,5,6]], dtype=numpy.int8)
# print(a.flags)

# 创建数组
x = numpy.empty([3, 2], dtype=numpy.int)
print(x)

# 全是1
shape = [4,5]
allOne = numpy.ones(shape=shape, dtype=numpy.int)
print(allOne)

# 全是0
allAeros = numpy.zeros(shape=shape, dtype=float)
print(allAeros)

## 使用已有数据创造数组
temp = numpy.asarray(allAeros,dtype=numpy.int)
print(temp)

## 流创建数组
## b'123456789' str = > bytestring
n = numpy.frombuffer(b'123456789', dtype='S1')
n.shape = (3,3)
print(n)

## 迭代创建numpy对象
iterable = iter([1.2,3,4,5,67,8])
#  count=6 读取多少个数据
temp = numpy.fromiter(iterable, dtype=numpy.float, count=6)
print(temp)

## 数值范围内创建数组
temp = numpy.arange(start=0, stop=100)
print(temp)

## 数值范围内创建等差数组
temp = numpy.linspace(start=1.0, stop=2.0, num=10)
print(temp)

## 数值范围内创建等比数组
temp = numpy.logspace(start=0, stop=9, num=10, base=2, dtype=numpy.int)
print(temp)

