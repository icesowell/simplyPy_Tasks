class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if self.rating == other:
                return True
            return False
        elif isinstance(other, ChessPlayer):
            if self.rating == other.rating:
                return True
            return False
        return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            if self.rating > other:
                return True
            return False
        elif isinstance(other, ChessPlayer):
            if self.rating > other.rating:
                return True
            return False
        return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        b = self > other
        if b ==True:
            return False
        elif b == False:
            return True
        else:
            return 'Невозможно выполнить сравнение'


"""
test
magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)
print(ian == 2789)
print(magnus == ian)
print(magnus > ian)
print(magnus < ian)
print(ian < magnus)
print(ian < [1,2])

"""
