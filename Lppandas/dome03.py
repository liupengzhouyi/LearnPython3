
import pandas
import numpy


## 生成数据透视表

df = pandas.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                        'B': ['A', 'B', 'C'] * 4,
                        'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                        'D': numpy.random.randn(12),
                        'E': numpy.random.randn(12)})


print(df)

newDf = pandas.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

print(newDf)





## 51. 时间序列

rng = pandas.date_range('2/27/2020 00:00', periods=5, freq='D')

print(rng)

ts = pandas.Series(numpy.random.randn(len(rng)), rng)

print(ts)


## 时间表示形式修改

ts_utc = ts.tz_localize('UTC')

print(ts_utc)


## 其他时区
ts_utc = ts_utc.tz_convert('US/Eastern')

print(ts_utc)

## 调整时间
prng = pandas.period_range('1999Q1', '2000Q4', freq='Q-NOV')

print(prng)

ts = pandas.Series(numpy.random.randn(len(prng)), prng)

print(ts)
# 季度频率转换为下一季度月末上午 9 点
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts)