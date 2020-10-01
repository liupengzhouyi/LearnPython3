import pandas as pd
import matplotlib.pyplot as plt
import pylab

# 创建一个 10*20 的点, 分辨率 200
plt.figure(figsize=(40, 21), dpi=100)

df = pd.read_csv('sh600000.csv')

numberI = 0
number = 100

# 激活第一个 subplot
plt.subplot(3,  1,  1)
# 绘制第一个图像
plt.plot(df['date'][numberI:number],  df['open'][numberI:number], color='r')
plt.plot(df['date'][numberI:number],  df['high'][numberI:number], color='b')
plt.plot(df['date'][numberI:number],   df['low'][numberI:number], color='y')
plt.plot(df['date'][numberI:number], df['close'][numberI:number], color='g')

plt.subplot(3,  1,  2)

plt.bar(df['date'][numberI:number], (df['open'][numberI:number] - df['close'][numberI:number]), align = 'center')


lista = []
listb = []
for i in range(number):
    if df['open'][i] - df['close'][i] > 0 :
        lista.append(df['open'][i] - df['close'][i])
        listb.append(0.0)
    else:
        lista.append(0.0)
        listb.append(df['open'][i] - df['close'][i])

plt.subplot(3,  1,  3)

plt.bar(df['date'][numberI:number], lista, align = 'center', color='r')

listc = []
for item in listb:
    listc.append(0-item)

plt.bar(df['date'][numberI:number], listc, align = 'center', color='g')


plt.savefig('image002.png')

# 展示图像
plt.show()
