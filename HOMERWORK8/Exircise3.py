class Human:
    def __init__(self, name):
        self.name = name
    
    def name_a(self):
        print("{} ученик школы №24.".format(self.name))

class Student(Human):
    def __init__(self, name, homework):
        super().__init__(name)
        self.homework = homework

    def work(self):
        print('{} сдал {} домашних заданий.'.format(self.name, self.homework))

    def __lt__(std1, std2):
        return std1.homework < std2.homework 

    def __gt__(std1, std2):
        return std1.homework > std2.homework   

    def __eq__(std1, std2):
        return std1.homework == std2.homework
    
    def __ne__(std1, std2):
        return std1.homework != std2.homework

    def __le__(std1, std2):
        return std1.homework <= std2.homework

    def __ge__(std1, std2):
        return std1.homework >= std2.homework
    
Ivan = Student('Иван', '13')
Nicolay = Student('Никола', '18')

print("Иван > Николай : {}".format(Ivan.homework > Nicolay.homework))
print("Иван < Николай : {}".format(Ivan.homework < Nicolay.homework))
print("Иван >= Николай : {}".format(Ivan.homework >= Nicolay.homework))
print("Иван <= Николай : {}".format(Ivan.homework <= Nicolay.homework))
print("Иван == Николай : {}".format(Ivan.homework == Nicolay.homework))
print("Иван != Николай : {}".format(Ivan.homework != Nicolay.homework))
