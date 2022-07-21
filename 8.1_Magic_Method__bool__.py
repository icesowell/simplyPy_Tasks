class City:

    def __init__(self, City):
        self.name = str.title(City)

    def __str__(self):
        return f'Город: {self.name}'

    def __bool__(self):
        a = ['a', 'e', 'i', 'o', 'u']
        b = self.name[-1]
        for i in a:
            if b == i:
                return False
        return True

"""
test
p1 = City('new york')
print(p1)
print(bool(p1))
p2 = City('SaN fraNcisco')
print(p2)
print(bool(p2))

"""
