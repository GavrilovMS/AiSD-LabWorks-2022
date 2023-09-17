class Vector:
    def __init__(self, size = 0):
        self.capacity = size*2+1
        self.arr = [None]*self.capacity
        self.size = size

    def __str__(self):
        res = '['
        for i in range(self.size):
            res += str(self.arr[i])
            if i != self.size-1:
                res += ', '
        res += ']'
        return res

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if isinstance(index, slice):
            new_arr = Vector(self.size//4 + 1)
            new_arr.size = 0
            for i in range(index.start if index.start is not None else 0, \
                           index.stop if index.stop is not None else self.size,\
                           index.step if index.step is not None else 1):
                new_arr.push_back(self.arr[i])
            return new_arr
        else:
            if index >= self.size:
                return
            return self.arr[index]

    def __setitem__(self, index, data):
        if index >= self.size:
            return
        self.arr[index] = data

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

    def delete(self, index):
        if index >= self.size:
            print("Error")
            return
        else:
            self.arr[index:self.size-1] = self.arr[index+1:self.size]
            self.size-=1

    def last(self):
        return self.arr[self.size-1]

    def swap(self,in1,in2):
        self.arr[in1], self.arr[in2] = self.arr[in2], self.arr[in1]

    def max(self):
        if len(self) == 0:
            return 0
        return max(self.arr[:self.size])








