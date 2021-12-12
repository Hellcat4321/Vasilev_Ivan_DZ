def encodef (liste):
    """Функция получает строку и шефрует её.
    liste - аргумент, строка
    """
    for i in range(len(liste)):
        liste[i] = liste[i].encode('utf-8')
    return liste

def decodef (liste):
    """Функция получает строку и дешефрует её.
    liste - аргумент, строка
    """
    for i in range(len(liste)):
        liste[i] = liste[i].decode('utf-8')
    return liste

a = list()
stroka = ''

while True:
    stroka = input('Введите страку (для завершения введите "stop"): ')
    if stroka != 'stop':
        a.append(stroka)
    else:
        break

print('Ваша страка: {}'.format(a))
x = encodef(a)
print('Зашифрованная строка: {} '.format(x))
x = decodef(x)
print('Расшифрованная строка: {}'.format(x))