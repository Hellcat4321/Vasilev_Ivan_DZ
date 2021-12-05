import copy

def passwords(a):
    namber = 0
    if len(a) >= 6:  #Проверка на количество символов (не менее 6)
        for i in range(0 , len(a)):
            if a[i].isdigit(): #Подсчёт цифр в строке
                namber = namber+1;
            else:
                continue
        if(namber == len(a)): #Проверка на то, что пароль состоит не только из цифр
            return('False!')
        elif(namber  == 0): #Проверка на наличие хотя бы 1 цифры
            return('False!')
        else:
            d = copy.copy(a) #Создаю копию строки чтобы не испортить изначальную строку 
            d = d.lower()
            if 'password' in d : #Проверка на подстраку "password" в любом регистре!
                return('False!')
            else:
                return('True!')       
    else:
        return('False!')
            
print(passwords(a = input()))
