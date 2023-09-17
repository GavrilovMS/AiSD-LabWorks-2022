import LinkedList

class Stack:

    def __init__(self):
        self.list = LinkedList.LinkedList()

    def __str__(self):
        return str(self.list)

    def push_back(self, data):
        self.list.push_back(data)

    def pop_back(self):
        if self.list.size != 0:
            cur = self.list.tail.data
            self.list.remove(self.list.size - 1)
            return cur

    def last(self):
        if self.list.size != 0:
            return str(self.list.tail.data)

    def getsize(self):
        return self.list.getsize()
