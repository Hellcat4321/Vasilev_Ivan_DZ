class Animals:
    def __init__(self, name, colors, height, weight):
        self.name = name
        self.colors = colors
        self.height = height
        self.weight = weight

    def colors_a(self):
        print("Цвет {} - {}.".format(self.name, self.colors)) 
    
    def height_a(self):
        print("Рост {} - {} м.".format(self.name, self.height))
    
class Mammals(Animals):
    def __init__(self, name, colors, height, weight, food, arial):
        super().__init__(name, colors, height, weight)
        self.food = food
        self.arial = arial

    def food_m(self):
        print("{} ест {}.".format(self.name, self.food))

class Human(Mammals):
    def __init__(self, name, colors, height, weight, food, arial, income):
        super().__init__(name, colors, height, weight, food, arial)
        self.income = income
    
    def income_a(self):
        print("Доход человека {} равен {}, и он ест {}.".format(self.name, self.income, self.food))

class Cat(Mammals):
    def __init__(self, name, colors, height, weight, food, arial, tail):
        super().__init__(name, colors, height, weight, food, arial)
        self.tail = tail

    def tail_m(self):
        print("У кошки {} хвост {} сантиметров в длинну.".format(self.name, self.tail))

class Dog(Mammals):
    def __init__(self, name, colors, height, weight, food, arial, bone):
        super().__init__(name, colors, height, weight, food, arial)
        self.bone = bone

    def bone_m(self):
        print("У собаки {} есть {} косточка.".format(self.name, self.bone))

Animal = Animals("Животное", "Розовое", 1.5, 40)
print(Animal.name)
Animal.colors_a()
Animal.height_a()

Mammal = Mammals("Млекопитающие", "Красные", 1.0, 60, "Траву", "Лес")
print("\n"+Mammal.name)
Mammal.food_m()

Ivan = Human("Иван", "Зелёный", 1.3, 70, "Чипсы", "Ярославль", 1000)
print("\n"+Ivan.name)
Ivan.income_a()

Vasia = Cat("Вася", "Чёрный", 0.3, 5, "Рыбу", "В квартире у Ивана", 35)
print("\n"+Vasia.name)
Vasia.tail_m()

Bobic = Dog("Бобик", "Белый", 0.6, 15, "Мясо", "В квартире у Ивана", 12)
print("\n"+Bobic.name)
Bobic.bone_m()