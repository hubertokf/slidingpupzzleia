class Queue(object):
    def __init__(self):
        self.data = []

    def push(self, e):
        self.data.append(e)

    def pop(self):
        return self.data.pop(0)

    def empty(self):
        return len(self.data) == 0
