import Vector

class Stack:

    def __init__(self):
        self.arr = Vector.Vector()

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, index):
        return self.arr[index]

    def push_back(self, data):
        self.arr.push_back(data)

    def pop_back(self):
        if self.arr.size != 0:
            cur = self.arr[self.arr.size-1]
            self.arr.delete(self.arr.size - 1)
            return cur

    def last(self):
        if self.arr.size != 0:
            return self.arr[self.arr.size-1]


