class Building:
    def __init__(self, floors):
        self.build = [None for i in range(floors)]

    def __getitem__(self, item):
        return self.build[item]

    def __setitem__(self, key, value):
        self.build[key] = value

    def __delitem__(self, key):
        del self.build[key]


"""
test

iron = Building(22)
iron[0] = 'Reception'
iron[1] = 'Oscar'
iron[2] = 'Stark Building'
print(iron[2])
del iron[2]
print(iron[2])

"""
