a = input("Enter the first number = ")
b = input("Enter the second number = ")

print("Результат сложения двух чисел = {}"
                .format(float(a) + float(b)))

print("Результат вычитания двух чисел = {} или {}".
                format(float(a) - float(b), float(b) - float(a)))

print("Результат умножения двух чисел = {}"
                .format(float(a) * float(b)))

if (float(a) == 0): 
    print("Результат деления двух чисел = {}"
                .format(float(a) / float(b)))
elif(float(b) == 0): 
    print("Результат деления двух чисел = {}"
                .format(float(b) / float(a)))
else: 
    print("Результат деления двух чисел = {} или {}"
                .format(float(a) / float(b), float(b) / float(a)))

print("Результат возведения в степень двух чисел = {} или {}"
                .format(float(a)**float(b), float(b)**float(a)))

if (float(a) == 0): 
    print("Результат деления по модулю двух чисел = {}"
                .format(float(a) / float(b)))
elif (float(b) == 0): 
    print("Результат деления по модулю двух чисел = {}"
                .format(float(b) / float(a)))
else: 
    print("Результат деления по модулю двух чисел = {} или {}"
                .format(float(a) % float(b), float(b) % float(a)))

if (float(a) == 0): 
    print("Результат целочисленного деления двух чисел = {}"
                .format(float(a)//float(b)))
elif (float(b) == 0): 
    print("Результат целочисленного деления двух чисел = {}"
                .format(float(b)//float(a)))
else:
    print("Результат целочисленного деления двух чисел = {} или {}"
                .format(float(a)//float(b), float(b)//float(a)))