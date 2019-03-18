#!/usr/bin/python3.7

# 我们的python是很不错的，但是
# 我在函数的传递参数的区域遇到了问题，
# 担忧我想我需要做一个关于Python的传递参数的问题

# 此实例传递不可变的对象
def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2

# 实例中有 int 对象 2，
# 指向它的变量是 b，
# 在传递给 ChangeInt 函数时，
# 按传值的方式复制了变量 b，
# a 和 b 都指向了同一个 Int 对象，
# 在 a=10 时，
# 则新生成一个 int 值对象 10，
# 并让 a 指向它。



# -----------------------------------

# 此实例中的可变对象实例

def changem(myList):
    myList.append([1, 3, 5])
    print(myList)
    # return

list = [10,34, '123']
changem(list)

print(list)


