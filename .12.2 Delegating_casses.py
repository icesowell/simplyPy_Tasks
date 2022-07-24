from functools import total_ordering


class Initialization:
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            if isinstance(food, list):
                self.food = food
        else:
            print('Кол-во людей должно быть целым числом')


class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super(MeatEater, self).__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают есть мясо! Они предпочитают есть {self.food}!'


class Vegan(Initialization):
    def __init__(self, capacity, food):
        super(Vegan, self).__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}!'


@total_ordering
class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super(SweetTooth, self).__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return other == self.capacity
        elif isinstance(other, (MeatEater, Vegan)):
            return other.capacity == self.capacity
        return f'Невозможно сравнить колличество сладкоежек со значением {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        elif isinstance(other, (MeatEater, Vegan)):
            return self.capacity < other.capacity
        return f'Невозможно сравнить колличество сладкоежек со значением {other}'

"""

test 

v = Vegan(1000, ['Орехи', 'Фрукты'])
print(v)
a = Vegan([23], ['nothing'])
m = MeatEater(15000, ["Жареная кортошка", "Рыба"])
print(m)
s = SweetTooth(30000, ['мороженое', 'чипсы', 'шоколад'])
print(s)
print(s > m)
print(s > v)
print(s == m)
print(30000 == s)
print(s == 25000)
print(10000000 < s)
print(100 < s)
print(s == 'sad')


"""
