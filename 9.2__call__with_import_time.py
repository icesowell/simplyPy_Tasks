from time import perf_counter


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        self.func()
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')


@Timer
def calculate():
    b = 0
    for i in range(0, 10_000_000):
        2 ** 100
    print(b)


calculate()
