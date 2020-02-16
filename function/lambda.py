
# lambda

# 匿名函数

# lambda x, y : x + y

def f(x, y):
    return lambda: x * 5

k = f(2, 4)

print(k())

L = list(map(lambda x: x * x, [1,2,3]))

print(L)


LL = list(filter(lambda x: x%2==0, [x for x in range(20)]))

print(LL)