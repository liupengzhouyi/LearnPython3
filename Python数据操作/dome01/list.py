classMates = ['没有！','没有！！','没有！！！', "temp"]

for i in classMates:
    print(i)

for i in range(len(classMates)):
    print(classMates[i])

# add
classMates.insert(0, "123")
classMates.insert(len(classMates)+1, "1234")
classMates.append("temp")

for i in range(len(classMates)):
    print(classMates[i])

# delete
classMates.pop(0)
print(classMates)

# update
classMates[0] = "有！"
print(classMates)

for i in range(len(classMates)):
    if (classMates[i] == "有！"):
        classMates[i] = "没有！"
        break

print(classMates)

# select
if("1234" in classMates):
    print("存在一个1234于list中")

if("12345" not in classMates):
    print("不存在一个12345于list中")

print(classMates.count("temp"))

print(classMates.index("temp"))