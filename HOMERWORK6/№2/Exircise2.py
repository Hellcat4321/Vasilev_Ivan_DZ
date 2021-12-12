import re

molecul = 0
try:
    with open('HOMERWORK6\№2\input.txt', 'r') as file:
        #Считываем данные из файла и заносим в переменные
        data = file.read()
        data = re.split('C:| H:| O:|" "', data)
        Carbon = int(data[1])
        Hydrogen = int(data[2])
        Oxygen = int(data[3])      
except FileNotFoundError:
    print('Файл не найден!')
except ValueError:
    print('Не верные данные! Введите целое число!')

try:
    while True:
        if (Carbon >= 2 and Hydrogen >= 6 and 
                Oxygen >= 1):
            molecul += 1
            Carbon -= 2
            Hydrogen -= 6
            Oxygen -= 1
        else:
            break
except NameError:
    print('Не правильно введены значения!')

with open('HOMERWORK6\№2\output.txt', 'w') as file:
    file.write('Molecul = {}'.format(molecul))