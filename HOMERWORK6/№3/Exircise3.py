def xor(str,key):
    try:
        str1 = ''
        for i in str:
            str1 += chr(ord(i) ^ key)
        return str1
    except ValueError:
        print('Ключ должен быть целым числом!')

new_string = ''

try:   
    with open('HOMERWORK6\№3\input.txt', 'r') as file:
        new_string = file.read()
except FileNotFoundError:
    print('Файл не найден!')

print('Данные из файла:{}'.format(new_string))
try:
    key = int(input('Введите ключ: '))
    new_string = xor(new_string, key)
    shif_string = xor(new_string, key)
    with open('HOMERWORK6\№3\output.txt', 'w') as file:
            file.write('Zashifrovannaya stroka: {}  c key: {}\n'.format(new_string,key))
            file.write('Deshifrovannaya stroka: {}  c key: {}'.format(shif_string,key))
            
except UnicodeEncodeError:
    print('Данный ключ не существует!')
except ValueError:
    print('Ключ должен быть целым числом!')
