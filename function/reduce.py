from functools import reduce

l = [x+1 for x in range(10)]
print(l)

def f(a, b):
    print('a =', a, 'b =', b, 'a + b =', a + b)
    return a + b

L = reduce(f, l)
print(L)

# string to int

def ff(x, y):
    return x * 10 + y

def fff(x):
    return int(x)

def ffff(x):
    return float(x)

print(reduce(ff, map(fff, '1234567')) + 1)

ss = '1234567.1234'
s1 = ss[:ss.index('.')]
print(s1)
s2 = ss[ss.index('.')+1:]
print(s2)

# 1234 => 0.1234

# 4321 => 0.1234
def fffff(a, b):
    return float(a) / 10 + float(b)


print(reduce(fffff, s2[::-1]) / 10)






