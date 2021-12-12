def summar(*arge):
    """Функция суммирует все элементы,
    которые в неё входят. 
    """
    try: 
        return sum(arge)
    except TypeError:
        print('Должны быть введены числа!')
        return 
    
print('Сумма 1 равна {}.'.format(summar(1, 2, 3, 4, 5, 6)))
print('Сумма 2 равна {}.'.format(summar('das', 'saa', 'A')))
print('Сумма 3 равна {}.'.format(summar(1, 2, 3)))
print('Сумма 4 равна {}.'.format(summar(1.5, 1.22, 3.0)))
print('Сумма 5 равна {}.'.format(summar()))
