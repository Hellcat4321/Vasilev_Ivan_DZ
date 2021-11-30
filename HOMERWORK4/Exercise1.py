import random

a =list()
for i in range(0, 10):
    a.append(random.randint(0,99))
print("Ваши массив: {}".format(a))

for j in range(0,9):
    for i in range(0,9):
        if a[i] > a[i+1]:
            x = a[i]
            a[i]=a[i+1]
            a[i+1]=x
print("Ваши отсортированный массив: {}".format(a))