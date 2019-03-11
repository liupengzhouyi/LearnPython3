
def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a + b
        max = max - 1
        # print(b)
        yield r

# yield有什么用？

# 在这个程序中，返回r给print(i),执行万能之后，继续下一句



# using generrator

for i in fib(5):
    print(i)