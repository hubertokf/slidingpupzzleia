class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if not self.empty():
            return self.data.pop(-1)

    def empty(self):
        return len(self.data) == 0
