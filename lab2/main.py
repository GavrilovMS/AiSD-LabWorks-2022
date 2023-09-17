from TimSort import tim_sort
from random import randint
from time import process_time
from Vector import Vector

def test(number_of_nums):
    time = process_time()
    arr = Vector(number_of_nums)
    for i in range(len(arr)):
        arr.change(i, randint(1, 1000))
    print("Array:")
    print(arr)
    tim_sort(arr)
    print("Sorted array:")
    print(arr)
    print("Time (in secs):", time)
    print()

test(0)
test(1)
test(2)
test(50)
test(100)
test(1000)






