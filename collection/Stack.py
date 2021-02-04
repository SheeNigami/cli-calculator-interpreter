class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack_list.pop(-1)

    def get(self):
        if self.isEmpty():
            return None
        return self.stack_list[-1]

    def isEmpty(self): 
        if len(self.stack_list) == 0: 
            return True
        return False
        

    def __str__(self):
        print(str(self.stack_list))
