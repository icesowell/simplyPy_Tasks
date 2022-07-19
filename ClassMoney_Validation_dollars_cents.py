class Money:
    def __init__(self, dollars, cent):
        self.total_cents = (dollars * 100) + cent

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, doll):
        if isinstance(doll, int) and doll >= 0:
            self.total_cents = self.cents + doll*100
        else:
            raise ValueError('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cent):
        if isinstance(cent, int) and cent < 100:
            self.total_cents = self.dollars*100 + cent
        else:
            raise ValueError('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} Долларов и {self.cents} Центов'

"""
test

Bill = Money(101, 99)
print(Bill)
Bill.dollars = 500
Bill.cents = 10
print(Bill)
"""
