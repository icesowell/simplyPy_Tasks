class Stack:
    def __init__(self):
        self.values = []

    def push(self, elem):
        self.values.insert(0, elem)

    def pop(self):
        if not self.is_empty() != False:
            return self.values.pop(0)
        return "empty stack"

    def peek(self):
        if not self.is_empty() != False:
            return self.values[0]
        return "empty stack"

    def is_empty(self):
        if len(self.values) != 0:
            return False
        return True

    def size(self):
        return len(self.values)

"""
test
s = Stack()
print(s.peek())
print(s.is_empty())
s.push('Cat')
s.push('Dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())
"""
