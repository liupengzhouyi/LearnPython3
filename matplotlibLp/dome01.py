import numpy
import matplotlib.pyplot
import pylab

x = numpy.linspace(-numpy.pi, numpy.pi, 1000, endpoint=True)
x = 3 * x
C, S = numpy.cos(x), numpy.sin(x)
k = numpy.linspace(0, 0, 1000, endpoint=True)

# 创建一个 8*6 的点, 分辨率 100
pylab.figure(figsize=(8, 2), dpi=200)

# 绘制一个 1x1 的图片
pylab.subplot(1, 1, 1)

matplotlib.pyplot.plot(x, C, color="blue", linewidth=3.0, linestyle='-', label='cos')
# matplotlib.pyplot.plot(x, k)
matplotlib.pyplot.plot(x, S, linestyle='-', label='sin')

# 添加图例
pylab.legend(loc='upper left')

# 设置横轴上下限
pylab.xlim(-15, 15)

# 设置横轴记号
pylab.xticks(numpy.linspace(-14, 14, 17, endpoint=True))

# 设置纵轴上下限
pylab.ylim(-1.2, 1.2)

# 解决坐标移动
o = pylab.gca()
o.spines['right'].set_color('none')
o.spines['top'].set_color('none')
o.spines['bottom'].set_position(('data', 0))
o.spines['left'].set_position(('data', 0))

# 坐标字重叠
for label in o.get_xticklabels() + o.get_yticklabels():
    label.set_fontsize(8)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

matplotlib.scatter(1, 2)

matplotlib.pyplot.show()
