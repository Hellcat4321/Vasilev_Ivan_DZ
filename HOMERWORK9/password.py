def password(a):
    """Функция проверяет правильность ввода строки 
    по определённым условиям.
    """

    namber = 0
    #Проверка на количество символов (не менее 6)
    if len(a) >= 6:  
        for i in range(0 , len(a)):
            #Подсчёт цифр в строке
            if a[i].isdigit(): 
                namber = namber + 1;
            else:
                continue
        #Проверка на то, что пароль состоит не только из цифр
        if(namber == len(a)): 
            return(False)
        #Проверка на наличие хотя бы 1 цифры
        elif(namber  == 0): 
            return(False)
        else:
            a = a.lower()
            #Проверка на подстраку "password" в любом регистре!
            if 'password' in a : 
                return(False)
            else:
                return(True)       
    else:
        return(False)