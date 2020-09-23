import numpy as np
import matplotlib.pyplot as plt

# 创建一个 10*20 的点, 分辨率 200
plt.figure(figsize=(10, 20), dpi=200)

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1

# 激活第一个 subplot
plt.subplot(3,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')

# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(3,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')

# 将第三个 subplot 激活，并绘制第三个图像
plt.subplot(3, 1, 3)
x =  [5,8,10]
y =  [12,16,6]

x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.savefig('image001.png')
# 展示图像
plt.show()

