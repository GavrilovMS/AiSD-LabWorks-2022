class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, size=0):
        self.head = None
        self.tail = None
        self.size = size
        if size != 0:
            self.head = Node()
            cur = self.head
            for i in range(0, size-1):
               cur.next = Node()
               cur = cur.next
               self.tail = cur

    def __str__(self):
        a = ""
        if self.size != 0:
            cur = self.head
            a = str(cur.data) + " "
            while cur.next is not None:
                cur = cur.next
                a += (str(cur.data) + " ")
            return a

    def push_back(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def getsize(self):
        return self.size

    def insert(self, index, data):
        if index > self.size:
            print("Error")
            return
        elif index == self.size:
            self.push_back(data)
        elif index == 0:
            cur = self.head
            self.head = Node(data)
            self.head.next = cur
        else:
            cur = self.head
            for i in range(0, index - 1):
                cur = cur.next
            next = cur.next
            new = Node(data)
            cur.next = new
            new.next = next
        self.size += 1

    def get(self, index):
        if index > self.size:
            print("Error")
            return
        else:
            cur = self.head
            for i in range(0, index):
                cur = cur.next
            return cur.data

    def remove(self, index):
        if index >= self.size:
            print("Error")
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(0, index-1):
                cur = cur.next
            if cur.next == self.tail:
                self.tail = cur
                self.tail.next = None
            else:
                cur.next = cur.next.next
        self.size-= 1





