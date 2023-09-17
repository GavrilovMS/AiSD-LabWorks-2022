class Vector:
    def __init__(self, size=0):
        self.capacity = size*2+1
        self.arr = [None]*self.capacity
        self.size = size

    def __str__(self):
        return str(self.arr[0:self.size])

    def getsize(self):
        return self.size

    def push_back(self, data):
        if self.size != self.capacity:
            self.arr[self.size] = data
        else:
            curarr = self.arr
            self.capacity*=2
            self.arr = [None]*self.capacity
            self.arr[0:self.size] = curarr[0:self.size]
            self.arr[self.size] = data
        self.size+=1

    def insert(self, index, data):
        if index > self.size:
            print("Error")
            return
        elif self.size != self.capacity:
            self.arr[index+1:self.size+1] = self.arr[index:self.size]
            self.arr[index] = data
            self.size += 1
        else:
            curarr = self.arr
            self.capacity*=2
            self.arr = [None]*self.capacity
            self.arr[0:index] = curarr[0:index]
            self.arr[index] = data
            self.arr[index + 1:self.size + 1] = curarr[index:self.size]
            self.size+=1

    def remove(self, index):
        if index >= self.size:
            print("Error")
            return
        else:
            self.arr[index:self.size-1] = self.arr[index+1:self.size]
            self.size-=1

    def get(self,index):
        if index >= self.size:
            print("Error")
            return
        else:
            return self.arr[index]

    def last(self):
        return self.arr[self.size-1]






