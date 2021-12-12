def fibonacci(a):
    """Функция возвращает число Фибоначчи по индексу.
    а - номер индекса числа Фибоначчи
    """
    if a == 0:
        return 0

    if a in (1, 2):
        return 1

    if a < 0:
        #Для отрицательных чисел
        return fibonacci(a + 2) - fibonacci(a + 1) 
    #Для положительных чисел
    return fibonacci(a - 1) + fibonacci(a - 2)  

try:
    a = int(input('Введите число Фибоначчи: '))
    print('Число Фибоначчи: {}.'.format(fibonacci(a)))
except ValueError:
    print('Введено не целое число!')
