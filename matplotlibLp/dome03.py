import pylab
import numpy


n = 1024
x = numpy.random.normal(0, 1, n)
y = numpy.random.normal(0, 1, n)

pylab.scatter(x, y)
pylab.show()
