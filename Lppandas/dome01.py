import numpy
import pandas

s = pandas.Series([1, 2, 3, 'oj', 'oio', 8, 90.23, 12])

print(s)

datas = pandas.date_range('20200226', periods=4)

print(datas)

df = pandas.DataFrame(numpy.random.randn(4, 3), index=datas, columns=list('127'))

print(df)


df2 = pandas.DataFrame(
    {
        'A': 1,
        'B': pandas.Timestamp('20200226'),
        'C': pandas.Series(1, index=list(range(4)), dtype=numpy.float32),
        'D': numpy.array([3] * 4, dtype=numpy.int),
        'E': pandas.Categorical(['test', 'train', 'test', 'train']),
        'F': 'foo',
    }
)


print(df2)

print(df2.head(2))


print(df2.tail(2))


print(df2.index)

print(df2.columns)

print(df2.to_numpy())

print(df2)
print(df2.T)

## 输出数据统计摘要

print(df2.describe())

print(df)

print(df.sort_index(axis=1, ascending=False))

print(df.sort_values(by='7'))

print(df['1'])

print(df)
# 0,1,2,3
# [1:3)
print(df[1:3])

print(df['2020-02-27':'2020-02-28'])


print(df)

## 用标签提取一行数据

print(df.loc[datas[0]])

## 用标签提取一列数据
print(df)

print(df.loc[:, '1'])

## 用标签提取多列数据
print(df)
print(df.loc[:, ['1', '2']])


print(df)
print(df.loc['2020-02-27':'2020-02-28', ['1', '2']])


print(df.loc['2020-02-27', ['1', '2']])

print(df)
print(df.loc['2020-02-27', '2'])
print(df.at['2020-02-27', '2'])

print(df)

print(df.iloc[2])

print(df)
print(df.iloc[[1, 2], [0, 2]])

print(df)
print(df.iloc[1:3, :])
print(df.iloc[1, 1])

print(df)
print(df[df['1'] > 0.0])

print(df)
print(df[df > 0.0])


df['8'] = [1, 2, 3, 4]
print(df)

print(df[df['8'].isin([2, 3])])

# 按标签赋值
df.at['2020-02-27', '8'] = 22
print(df)


# 按位置赋值
df.iat[0, 3] = 11
print(df)

# 按Numpy赋值
df.loc[:, '2'] = numpy.array([5] * len(df))
print(df)

# where赋值
df[df < 0] = df.abs()
print(df)

df = df[df > 1]
print(df)

df = df.fillna(value=0.56)
print(df)

## 统计
print(df.mean())

print(df.mean(1))


print(df)
print(df.apply(numpy.cumsum))

print(df.apply(lambda x: x.max() - x.min()))

ss = pandas.Series(['A', 'nihbi', 'ytgvhUGv', numpy.nan, 'ytuvyib', 12.90])
print(ss)

print(ss.str.lower())





















