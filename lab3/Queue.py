import Vector

class Queue:

    def __init__(self):
        self.list = Vector.Vector()

    def __str__(self):
        a = ""
        while self.list.size != 0:
            a += str(self.dequeue()) + " "
        return str(a)

    def __len__(self):
        return len(self.list)

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        if self.list.size != 0:
            cur = self.list.last()
            self.list.delete(len(self.list) - 1)
            return cur
