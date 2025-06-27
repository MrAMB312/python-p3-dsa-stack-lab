class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            print("Stack is full, cannot add more items.")
        else:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        for i in range (0, len(self.items)):
            if self.items[i] == target:
                return len(self.items) - (i + 1)
        return -1