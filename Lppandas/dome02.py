import pandas
import numpy

df = pandas.DataFrame(numpy.random.randn(10, 4))

print(df)

pieces = [df[:3], df[3:7], df[7:]]

for i in pieces:
    print(i)

df = pandas.concat(pieces)
print(df)

left = pandas.DataFrame({
    'key': ['foo', 'food'],
    'lval': [1, 2]
})

right = pandas.DataFrame({
    'key': ['foo', 'food'],
    'lval': [3, 4]
})

right1= pandas.DataFrame({
    'key': ['foo', 'food'],
    'lval': [5, 6]
})

print(left)

print(right)

newDf = pandas.merge(left, right, on='key')
print(newDf)

newDf = pandas.merge(newDf, right1, on='key')
print(newDf)

print(df)

s = df.iloc[3]
print(s)
df = df.append(s, ignore_index=True)
print(df)






















