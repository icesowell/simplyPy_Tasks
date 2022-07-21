from functools import total_ordering


@total_ordering
class Acc:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


"""
test 
ac1 = Acc(10)
ac2 = Acc(20)
print(ac1 > ac2)
print(ac1 < ac2)
print(ac2 > ac1)
print(ac1 != ac2)

"""
