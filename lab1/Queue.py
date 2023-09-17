import Vector

class Queue:

    def __init__(self):
        self.list = Vector.Vector()

    def __str__(self):
        a = ""
        while self.list.size != 0:
            a += str(self.dequeue()) + " "
        return str(a)

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        if self.list.size != 0:
            cur = self.list.last()
            self.list.remove(self.list.getsize() - 1)
            return cur

    def getsize(self):
        return self.list.getsize()
