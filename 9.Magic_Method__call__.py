class Addition:
    def __call__(self, *args, **kwargs):
        self.couter = 0
        for i in args:
            if isinstance(i, (int, float)):
                self.couter += i
        print(f'Сумма переданных аргументов = {self.couter}')

"""
test
add = Addition()
add(10, 20)
add(1, 2, 3.4)
add(1, 2, 'hello', [1, 2], 3)

"""
