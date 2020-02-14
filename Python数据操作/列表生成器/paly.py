myList = []
for i in range(20):
    myList.append(i+1)
print(myList)

myList1 = (range(1, 20))

print(myList1)
# for i in myList1:
#     print(i,)

## 新的玩法

myList2 = []
for x in range(1,10):
    myList2.append(x*3)
print(myList2)

# 比上一个高明的方法
myList3 = [x * 3 for x in range(1,10)]
print(myList3)

# 又是新的玩法
myList4 = [x + y + z for x in '123' for y in '789' for z in '456']
print(myList4)

# 遍历dict
# key -> value
temp1 = {'短程': 1000, '中程':5000, '长程':10000}

for k, v in temp1.items():
    print(k, '=>', v)




