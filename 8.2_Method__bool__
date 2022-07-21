class Quadrilateral:

    def __init__(self, *args):
        if len(args) >= 2:
            self.wigth = args[0]
            self.hight = args[1]
        else:
            self.wigth = args[0]
            self.hight = args[0]

    def __str__(self):
        if self.wigth == self.hight:
            return f'Куб размером: {self.wigth}x{self.hight}'
        return f'Прямоугольник размером: {self.wigth}x{self.hight}'

    def __bool__(self):
        if self.wigth == self.hight:
            return True
        return False

"""
#test 

p1 = Quadrilateral(10)
print(p1)
print(bool(p1))
p2 = Quadrilateral(3, 5)
print(p2)
print(bool(p2))
print(p2==True)

"""
