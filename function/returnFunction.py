

# return function

def returnFunction():
    def printSome():
        print("Hello World!")
    return printSome()

f = returnFunction

f()



# 闭包
def count1():
    fs = []
    for i in range(20):
        def p():
            return i * i
        fs.append(p)
    return fs

l = count1()

for i in l:
    print(i())

# 突破闭包

def count2():
    fs = []
    def p(i):
        def o():
            return i * i
        return o
    for i in range(20):
        fs.append(p(i))
    return fs

l2 = count2()

for i2 in l2:
    print(i2())