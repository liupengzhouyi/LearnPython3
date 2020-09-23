import pandas as pd
import matplotlib.pyplot as plt
import pylab

# 创建一个 10*20 的点, 分辨率 200
plt.figure(figsize=(20, 21), dpi=200)

df = pd.read_csv('sh600000.csv')

print(df)

print(df['date'])

print(df['open'])

# 激活第一个 subplot
plt.subplot(3,  1,  1)
# 绘制第一个图像
plt.plot(df['date'][0:100], df['open'][0:100], color='r')
plt.plot(df['date'][0:100], df['high'][0:100], color='b')
plt.plot(df['date'][0:100], df['low'][0:100], color='y')
plt.plot(df['date'][0:100], df['close'][0:100], color='g')

plt.subplot(3,  1,  2)
plt.bar(df['date'][0:100], (df['open'][0:100] - df['close'][0:100]), align = 'center')


lista = []
listb = []
for i in range(100):
    if df['open'][i] - df['close'][i] > 0 :
        lista.append(df['open'][i] - df['close'][i])
        listb.append(0.0)
    else:
        lista.append(0.0)
        listb.append(df['open'][i] - df['close'][i])

plt.subplot(3,  1,  3)
plt.bar(df['date'][0:100], lista, align = 'center', color='r')

listc = []
for item in listb:
    listc.append(0-item)

plt.bar(df['date'][0:100], listc, align = 'center', color='g')


plt.savefig('image002.png')

# 展示图像
plt.show()
