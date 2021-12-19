import logging
import time
import math

def my_decorator(func):
    def wrapper(a, b, c):
        logging.basicConfig(filename="HOMERWORK9\log.log", level=logging.INFO)
        logging.info("Program started")
        start_time = time.time()
        func(a, b, c)
        time.sleep(3)
        logging.info("Program done!")
        logging.info("--- {} seconds ---".format(time.time() - start_time))
    return wrapper

@my_decorator
def quadratic_equation(a, b, c):
    DES = b**2 - 4*a*c 

    if(DES > 0):
        x1 = (-1*b + math.sqrt(DES)) / (2*a)
        x2 = (-1*b - math.sqrt(DES)) / (2*a)
        print("Ваши корни: x1 = {}, x2 = {}".format(x1, x2))
    elif(DES == 0):
        x = (-b) / (2*a)
        print("Ваши корнь: x = {}".format(x))
    else:
        print("Отрицательный дискриминант! Решений нет.")

a = 0
b = 0
c = 0

f = print('Введите коэффициенты квадратного уравнения (ax^2+bx+c=0)')
a = int(input('Введите коэффициент при x^2: '))
b = int(input('Введите коэффициент при x: '))
c = int(input('Введите свободный член: '))


quadratic_equation(a, b, c)