# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(start=8, step=8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__')) # é um iterável (objeto a ser percorrido)
print('c1', hasattr(c1, '__next__')) # é um iterador (objeto que pega um item de cada vez)
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in r1:
    print(i)
