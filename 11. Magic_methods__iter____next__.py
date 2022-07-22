class PowerTwo:
    def __init__(self, value):
        if value >= 0:
            self.value = value
            self.spisok = [i for i in range(0, value + 1)]

    def __iter__(self):
        self.lett = -1
        return self

    def __next__(self):
        self.lett += 1
        if self.lett >= len(self.spisok):
            raise StopIteration
        return 2 ** self.spisok[self.lett]

# test
# iterator = PowerTwo(4)
# iterator2 = iter(iterator)
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))
# print(next(iterator2))
# 
# 
# 
# #for i in PowerTwo(10):
# #    print(i)
# 
