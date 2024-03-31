class Stack:
    def __init__(self, items=None, limit=None):
        self.stack = [] if items is None else items
        self.limit = limit

    def push(self, value):
        if self.limit is None or len(self.stack) < self.limit:
            self.stack.append(value)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def full(self):
        if self.limit is None:
            return False
        else:
            return len(self.stack) == self.limit

    def search(self, value):
        if self.is_empty():
            return -1
        elif value in self.stack:
            return len(self.stack) - self.stack.index(value) - 1
        else:
            return -1

    def isEmpty(self):
        return self.is_empty()
