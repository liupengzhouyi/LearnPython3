
# filter

L = [x + 3 for x in range(20)]

def isCon(x):
    if x % 2 == 0:
        return True
    else:
        return False

newL = filter(isCon, L)

while True:
    try:
        print(next(newL))
    except StopIteration:
        print(StopIteration.value)
        break



