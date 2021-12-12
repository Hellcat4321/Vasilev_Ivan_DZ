import random

a = set()
b = set()
for i in range(0, 10):
    a.add(random.randint(0, 20))
    b.add(random.randint(0, 20))
    
print('Первое множество: {}'.format(a))
print('Второе множество: {}'.format(b))
print('Элементы, которые входят одновременно в оба: {}'.format(a.intersection(b)))
print('Элементы, которые входят только в первое, но не входит во второе: {}'.format(a.difference(b)))
print('Элементы, которые входят только во второе, но не входит в первое: {}'.format(b.difference(a)))
print('Элементы, которые входит в первое или во второе, но не в оба из них одновременно: {}'.format(a.symmetric_difference(b)))
