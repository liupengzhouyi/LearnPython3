

print(sorted([34,-67,9,-8,7,12]))

print(sorted([34,-67,9,-8,7,12],key=abs))

print(sorted(['a', 'kihjb', 'L', 'ihkun', 'YVG'], key=str.lower))

print(sorted([34,-67,9,-8,7,12], reverse=True))

L = [('Lio', 13),('asd', 12)]

print(sorted(L, key = lambda t : str(t[0]).lower()))

print(sorted(L, key = lambda t : t[1], reverse=True))
