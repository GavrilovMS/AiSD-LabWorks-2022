import Stack
from Vector import *

def get_minrun(n):
    flag = 0
    while n >=64:
        flag |= n & 1
        n >>= 1
    return n + flag


def insertion_sort(elements, start, end):
    for i in range(start+1, end+1):
        j = i
        while j > start and elements.get(j-1) > elements.get(j):
            elements.swap(j, j-1)
            j -= 1


def merge(elements, start, mid, end, m):
    left = elements.get_section(start, mid+1)
    left.push_back(m)
    right = elements.get_section(mid+1, end+1)
    right.push_back(m)
    i = j = 0
    for k in range(start, end+1):
        if left.get(i) <= right.get(j):
            elements.change(k, left.get(i))
            i += 1
        else:
            elements.change(k,right.get(j))
            j += 1


def tim_sort(elements):
    n = len(elements)

    m = elements.max()+1
    minrun = get_minrun(n)
    stack = Stack.Stack()
    cur = 0

    if n == minrun:
        insertion_sort(elements,0,n-1)
        return

    while cur != n:
        cur_end = cur + minrun - 2
        if cur_end >= n:
            cur_end = n-1
        if cur_end != n - 1 and elements.get(cur_end-1) > elements.get(cur_end):
            while cur_end != n - 1 and elements.get(cur_end-1) > elements.get(cur_end):
                cur_end += 1
        else:
            while cur_end != n - 1 and elements.get(cur_end-1) <= elements.get(cur_end):
                cur_end += 1
        stack.push_back([cur, cur_end-cur+1])

        insertion_sort(elements, cur, cur_end)
        cur = cur_end+1

        s1 = stack.get(len(stack) - 1)[0]
        s2 = stack.get(len(stack) - 2)[0] if len(stack) > 1 else 0
        s3 = stack.get(len(stack) - 3)[0] if len(stack) > 2 else 0

        len1 = stack.get(len(stack) - 1)[1]
        len2 = stack.get(len(stack) - 2)[1] if len(stack) > 1 else n
        len3 = stack.get(len(stack) - 3)[1] if len(stack) > 2 else n

        if (len3 <= len2 + len1 or len2 <= len1):
            if len1 < len3:
                merge(elements, s2, s1 - 1, s1 + len1 - 1, m)
                stack.arr.arr[len(stack) - 2][1] += stack.arr.arr[len(stack) - 1][1]
                stack.pop_back()
            else:
                merge(elements, s3, s2 - 1, s2 + len2 - 1, m)

                stack.arr.arr[len(stack) - 3][1] += stack.arr.arr[len(stack) - 2][1]
                temp = stack.pop_back()
                stack.pop_back()
                stack.push_back(temp)

