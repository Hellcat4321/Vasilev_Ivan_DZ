invent = dict()
action = 0
ollweight = 0
object = 0
weight = 0

print("Добро пожаловать в менеджмент инвентаря!")

while 1:
    action = (input("Что сделать с инвентарём? '1'- добавляем предмет в инвентарь; '2'- удаляем предмет из инвентаря; '3'- выходим из инвентаря. "))
    
    if action.isdigit():
        action = int(action)
    else:
        print("Такой команды не существует! ")
        continue

    if action == 1:

        if ollweight == 100:
            print("Вы несёте максимальный вес. Удалите предметы из инвентаря, чтобы взять новые! ")
            print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                    invent, ollweight))
            continue

        object = input("Введите название предмета: ")

        if invent.get(object) != None:
            weight = invent.pop(object)
            ollweight -= weight

            weight = (input("Введите вес предмета '{}' в килограммах: ".format(object)))
            
            if weight.isdigit():
                weight = int(weight)
            else:
                print("Вес предмета должен быть целым числом! ")
                print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                        invent, ollweight))
                continue

            if (ollweight + weight > 100):
                print("Данный предмет вам не по силам. Облегчите инвентарь!")
                print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                        invent, ollweight))
                continue
            else:
                invent[object] = weight
                ollweight += weight
        else:
            weight = (input("Введите вес предмета '{}' в килограммах: ".format(object)))

            if weight.isdigit():
                weight = int(weight)
            else:
                print("Вес предмета должен быть целым числом! ")
                print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                        invent, ollweight))
                continue
            
            if (ollweight + weight > 100):
                print("Данный предмет вам не по силам. Облегчите инвентарь!")
                print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                        invent, ollweight))
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
                print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                                    invent, ollweight))
                continue
            else:
                print("Предмет '{}' удален. ".format(object))
                weight = invent.pop(object)
                ollweight -= weight

    elif action == 3:
        print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг. ".format(
                                                                invent, ollweight))
        break
    else:
        print("Такой команды не существует! ")
        continue
    
    print("\nВаш инвентарь {}, Общий вес инвентаря {}кг из 100кг.\n ".format(
                                                            invent, ollweight))
    