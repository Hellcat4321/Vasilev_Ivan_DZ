import math
import cmath

a = int(input('Введите коэффициент при x^2: '))
b = int(input('Введите коэффициент при x: '))
c = int(input('Введите свободный член: '))

DES = b**2 - 4*a*c 

if(DES > 0):
    x1 = (-1*b + math.sqrt(DES)) / (2*a)
    x2 = (-1*b - math.sqrt(DES)) / (2*a)
    print("Ваши корни: x1 = {}, x2 = {}".format(x1, x2))
elif(DES == 0):
    x = (-b)/(2*a)
    print("Ваши корнь: x = {}".format(x))
else:
    x1 = complex((-b + cmath.sqrt(DES)) / (2*a))
    x2 = complex((-b - cmath.sqrt(DES)) / (2*a))
    print("Ваши комплексные корни: x1 = {}, x2 = {}".format(x1, x2))