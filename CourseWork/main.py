from Kruskal import Kruskal
from Vector import Vector

def get_matrix():
    s = ''
    with open('matrix.txt', 'r') as f:
        s = f.read().split()
    matrix = Vector()
    temp_arr = Vector()
    n = 0
    while not s[0].isnumeric():
        temp_arr.push_back(s.pop(0))
        n += 1
    matrix.push_back(temp_arr)
    temp_arr = Vector()
    for i in range(len(s)):
        temp_arr.push_back(s[i])
        if i % n == 2:
            matrix.push_back(temp_arr)
            temp_arr = Vector()
    return matrix

def get_lists_v_e():
    m = get_matrix()
    v = m[0]
    n = len(m) - 1
    res = Vector()
    temp_arr = Vector(3)
    for i in range(1, n+1):
        for j in range(n):
            if int(m[i][j]) > 0:
                temp_arr[0] = m[0][i-1]
                temp_arr[1] = m[0][j]
                temp_arr[2] = m[i][j]
                res.push_back(temp_arr)
                temp_arr = Vector(3)
    return v,res

def main():
    v, e = get_lists_v_e()
    e = Kruskal(e, v)

    sum = 0
    for i in range(len(e)):
        print(e[i][0] + ' ' + e[i][1])
        sum += int(e[i][2])

    print(sum)

if __name__ == '__main__':
    main()