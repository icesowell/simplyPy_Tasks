class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values.sort()

    def __str__(self):
        if len(self.values) > 0:
            b = [str(i) for i in self.values]
            return f'Вектор ({", ".join(b)})'
        return 'Вектор пустой'

    def __add__(self, other):
        new_wa = []
        if isinstance(other, (int, float)):
            for i in range(0, len(self.values)):
                new_wa.append(self.values[i] + other)
        elif isinstance(other.values, list) and len(other.values) == len(self.values):
            for i in range(0, len(self.values)):
                new_wa.append(self.values[i] + other.values[i])
        elif isinstance(other, list) and len(other) != len(self.values):
            print('Сложение векторов разной длинны недопустимо')
        elif isinstance(other, Vector) and len(other.values) == len(self.values):
            for i in range(0, len(self.values)):
                self.values[i] = self.values[i] + (other.values[i])
                return self.values
        elif not isinstance(other, (list, int)):
            return 'Вектора разных типов нельзя сложить '
        return new_wa

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        new_wa2 = []
        if isinstance(other, (int, float)):
            for i in range(0, len(self.values)):
                new_wa2.append(self.values[i] * other)
        elif isinstance(other, list) and len(other) == len(self.values):
            for i in range(0, len(self.values)):
                new_wa2.append(self.values[i] * other[i])
        elif isinstance(other, list) and len(other) != len(self.values):
            print('Умножение векторов разной длинны недопустимо')
        elif isinstance(other, Vector) and len(other.values) == len(self.values):
            for i in range(0, len(self.values)):
                self.values[i] = self.values[i] * (other.values[i])
        elif not isinstance(other.values, (list, int)):
            print('Вектора разных типов нельзя умножить ')
        return new_wa2

"""
test 
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v3 = v1 + v2
print(v3)
v3 = v1 * 2
print(v3)

"""
