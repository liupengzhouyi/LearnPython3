#define a Fib class

class Fib(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

# 因为我们实现了next函数，所以我们可以使用这个类：当迭代器

# Using Fib object

for i in Fib(90):
    print(i)

