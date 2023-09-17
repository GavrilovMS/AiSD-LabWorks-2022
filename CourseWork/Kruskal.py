from DisjointSet import DisjointSet
from Vector import Vector

def sort_edges(edges):
    for i in range(len(edges)-1):
        for j in range(i+1, len(edges)):
            if edges[i][2] > edges[j][2]:
                edges[i], edges[j] = edges[j], edges[i]

def Kruskal(e, v):
    result = Vector()
    ds = DisjointSet()
    ds.makeSet(v)
    sort_edges(e)

    for i in range(len(e)):
        if ds.find(e[i][0]) != ds.find(e[i][1]):
            ds.union(e[i][0],e[i][1])
            result.push_back(e[i])

    return result
