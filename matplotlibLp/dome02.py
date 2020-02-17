from pylab import *
import numpy
n = 256
x = numpy.linspace(-numpy.pi, numpy.pi, n, endpoint=True)
y = numpy.sin(x)

plot(x, y, color='red', alpha=1.00)

show()