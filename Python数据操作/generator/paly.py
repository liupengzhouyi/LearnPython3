L = [x for x in range(20)]
print(L)

# create
g = (x for x in range(20))
# for i in range(30):
#     print(next(g))

# select
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as sError:
        print(sError.value)
        break

# a other way to create it
def fib(max):
    a = 1
    b = 1
    while b < max:
        print('-------begin!----------')
        yield b
        print('-------------- every time run it, stop!! ------')
        a, b = b, a + b

temp = fib(10)

print(1)
while True:
    try:
        print('-------begin----------')
        print(next(temp))
        print('-------------- every time run it, stop! ------')
    except StopIteration as sError:
        print(sError.value)
        break
