def fibonacci(a):
    if a == 0:
        return 0
    if a in (1, 2):
        return 1
    if a < 0:
        return fibonacci(a + 2) -- fibonacci(a + 1) #Для отрицательных чисел
    return fibonacci(a - 1) + fibonacci(a - 2)  #Для положительных чисел

try:
    a = int(input('Введите число Фибоначчи: '))
    print('Число Фибоначчи: {}.'.format(fibonacci(a)))
except ValueError:
    print('Введено не целое число!')
