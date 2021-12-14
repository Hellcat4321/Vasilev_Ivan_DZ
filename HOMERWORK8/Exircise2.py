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

Ivan = Student('Иван', '13')
Ivan.work()

Nicolay = Student('Никола', '18')
Nicolay.work()