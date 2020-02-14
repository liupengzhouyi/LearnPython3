from collections.abc import Iterator

L = [x for x in range(20)]
for i in range(len(L)):
    print(L[i])

# 是否可迭代
print(isinstance(L, Iterator))

# 变成 可迭代的数据
L = iter(L)
print(isinstance(L, Iterator))

# 如何迭代
while True:
    try:
        print(next(L))
    except StopIteration as error:
        print("_", error.value)
        break




