class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)
        self.size = self.size + 1

    def pop(self):
        self.size = self.size - 1
        return self.items.pop()
        

    def peek(self):
        return self.items[len(self.items) - 1]

    def sizes(self):
        return self.size


s = Stack()
s.push(8.4)
s.push(3.6)
print(s.sizes())
print(s)