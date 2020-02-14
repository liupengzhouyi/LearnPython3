
# []
# ()
# '1234567890'
# myList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
myList = []
for i in range(20):
    myList.append(i+1)
# myList = '1234567890'
print(myList)



# 输出前三个

#a way
print(myList[0], myList[1], myList[2])

# other way
for i in range(3):
    print(myList[i])

# last way
print(myList[0:3])

print(myList[:3])

print(myList[4:9]) # [)

# 倒着输出

## 倒数第一个
print(myList[-1:])

## 倒数第10名到第6名
print(myList[-10:-6])

## 取前10个数，每2个取1个
print(myList[0:10:2])
print(myList[1:10:2])

## 每5个取1个
print(myList[::5])

## all
print(myList[:])
print(myList[::])