invent = dict()
action = 0
ollweight = 0
object = 0
weight = 0
print("Добро пожаловать в менеджмент инвентаря!")
while 1:
    action = int(input("Что сделать с инвентарём? '1'- добавляем предмет в инвентарь; '2'- удаляем предмет из инвентаря; '3'- выходим из инвентаря. "))
    if action == 1:
        if ollweight == 100:
            print("Вы несёте максимальный вес. Удалите предметы из инвентаря, чтобы взять новые! ")
            print()
            print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))
            print()
            continue    
        object = input("Введите название предмета: ")
        weight = (input("Введите вес предмета '{}' в килограммах: ".format(object)))
        if weight.isdigit(): 
            weight = int(weight)
        else:
            print("Вес предмета должен быть целым числом! ")
            print()
            print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))
            print()
            continue
        if (ollweight + weight > 100):
            print("Данный предмет вам не по силам. Облегчите инвентарь!")
            print()
            print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))
            print()
            continue
        else:
            invent[object] = weight
            ollweight += weight
    elif action == 2:
        if ollweight == 0:
             print("Инвентарь пуст! ")
        else:
            object = input("Введите название предмета для удаления: ")
            if invent.get(object) == None:
                print("Предмет в инвенторе не найден! ")
                print()
                print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))
                print()
                continue
            else:
                print("Предмет '{}' удален. ".format(object))
                weight = invent.pop(object)
                ollweight -= weight

    elif action == 3:
        break
    else:
        print("Такой команды не существует! ")
        continue
    print()
    print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))
    print()
print()
print("Ваш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(invent,ollweight))    
        
