from AssociativeArray import AssociativeArray

class DisjointSet:
    def __init__(self):
        self.parent = AssociativeArray()

    def makeSet(self, v):
        for i in range(len(v)):
            self.parent[v[i]] = v[i]

    def find(self, k):
        if self.parent[k] == k:
            return k
        return self.find(self.parent[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent[x] = y