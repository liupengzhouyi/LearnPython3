import numpy

a = numpy.arange(12).reshape(3, 4)

b = numpy.arange(24,36).reshape(3, 4)

c = numpy.concatenate((a, b), axis = 1)
print(c)

d = numpy.concatenate((a, b), axis= 0)

print(d)