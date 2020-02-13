
# 路的种类
temp = {1: '山路', 2: '水泥路', 3:'柏油路'}

# add
temp[4] = '大海'

# (键-值)对儿
# key - value
# 距离
temp1 = {'短程': 1000, '中程':5000, '长程':10000}

# 是否负重
temp2 = {'是': 1, '否': 0}

# 负重重量
temp3 = {'轻':20, '适当':50, '重':100}

class Person:
    def __init__(self, type, distance, isAdd, addType):
        self.type = type,
        self.distance = distance
        self.isAdd = isAdd
        self.addType = addType

    def say(self):
        print('参加', self.distance, '米', self.type, '越野赛',)
        print('问；是否负重')
        if(self.isAdd == 1):
            print('是')
            print('负重', self.addType, '千克')
        else:
            print('否')

# update
temp[1] = '飞机跑道'

# select
me = Person(temp[1], temp1['中程'], temp2['是'], temp3['重'])
me.say()

temp[2] = '游泳'
me1 = Person(temp[2], temp1['短程'], temp2['否'], temp3['重'])
me1.say()

# print(temp[6])


# delete
print(temp)
temp.pop(3)
print(temp)
