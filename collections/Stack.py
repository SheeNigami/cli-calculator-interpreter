class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, value):
        self.stacklist.append(value)

    def pop(self):
        return self.stacklist.pop(-1)

    def get(self):
        return self.stacklist[-1]

    def __str__(self):
        print(str(self.stacklist))