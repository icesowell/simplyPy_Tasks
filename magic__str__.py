class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == 'female' or gender == 'male':
            self.gender = gender
        else:
            print('Не знаю что вы имели ввиду? Пусть это будет мальчик')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        elif self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'

""" 
test
p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)
p3 = Person('Оби-ван', 'Кеноби', True)
print(p3)
""" 
