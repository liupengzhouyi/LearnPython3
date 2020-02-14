
def run(x):
    return '今天走' + x + '千米'

# print(run('5'))

r = map(run, ['1', '2', '3', '4', '5', '6'])

while True:
    try:
        print(next(r))
    except StopIteration as error:
        break