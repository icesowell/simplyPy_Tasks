class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if len(self.values)>0:
            sorted_value = sorted(self.values)
            return f'Вектор {sorted_value}'
        return 'Вектор пустой'

"""
test

v1 = Vector(1,10, 2, 3,5)
print(v1)
v2 = Vector('safsf', 244, 2.3)
print(v2)
v3 = Vector()
print(v3)


"""
