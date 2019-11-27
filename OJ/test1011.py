



def test(a, b, c):
    d = str(float('%.2f' % float((a + b + c) / 3)))
    print(a+b+c, a*b*c, d)
a, b, c = map(int, input().split())
test(a, b, c)