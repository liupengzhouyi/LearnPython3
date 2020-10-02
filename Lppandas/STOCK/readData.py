import pandas as pd
import matplotlib.pyplot as plt
import pylab

# 创建一个 10*20 的点, 分辨率 200
plt.figure(figsize=(20, 24), dpi=200)

df = pd.read_csv('../stockData/sh600000.csv')

print(df)

print(df['date'])

print(df['open'])

# 激活第一个 subplot
plt.subplot(4,  1,  1)
# 绘制第一个图像
plt.plot(df['date'][0:20], df['open'][0:20], color='r')
plt.title('open')

# 激活第一个 subplot
plt.subplot(4,  1,  2)
# 绘制第一个图像
plt.plot(df['date'][0:20], df['high'][0:20], color='b')
plt.title('high')

# 激活第一个 subplot
plt.subplot(4,  1,  3)
# 绘制第一个图像
plt.plot(df['date'][0:20], df['low'][0:20], color='y')
plt.title('low')

# 激活第一个 subplot
plt.subplot(4,  1,  4)
# 绘制第一个图像
plt.plot(df['date'][0:20], df['close'][0:20], color='g')
plt.title('close')


plt.savefig('image001.png')

# 展示图像
plt.show()
