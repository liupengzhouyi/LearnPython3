

def ppp(x):
    print(x)

l = ppp
l("唤老白进宫！")

def p(x):
    def pp():
        print('---------传旨---------')
        ppp(x)
        print('---------钦此---------')
    return pp

ll = p("唤老白进宫！")
#  ll = pp
ll()

s = '1234567890'
for i in s:
    if i == '1':
        p(i)()
    elif i == '0':
        p(i)()
    else:
        ppp(i)