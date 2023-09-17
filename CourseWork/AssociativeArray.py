from Vector import Vector

class AssociativeArray:
    def __init__(self):
        self.__arr = Vector()

    def __len__(self):
        return len(self.__arr)

    def __str__(self):
        res = '['
        for i in range(len(self.__arr)):
            res += str(self.__arr[i][0]) + ': '+ str(self.__arr[i][1])
            if i != len(self.__arr) - 1:
                res += ', '
        res += ']'
        return res

    def __getitem__(self, key):
        for i in range(len(self.__arr)):
            if self.__arr[i][0] == key:
                return self.__arr[i][1]
        return

    def __setitem__(self, key, data):
        for i in range(len(self.__arr)):
            if self.__arr[i][0] == key:
                self.__arr[i][1] = data
                return
        new = Vector(2)
        new[0] = key
        new[1] = data
        self.__arr.push_back(new)
        return

    def delete_key(self, key):
        for i in range(len(self.__arr)):
            if self.__arr[i][0] == key:
                self.__arr.delete(i)
                return

    def delete_data(self, data):
        for i in range(len(self.__arr)):
            if self.__arr[i][1] == data:
                self.__arr.delete(i)
                return