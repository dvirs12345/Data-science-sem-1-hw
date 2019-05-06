import numpy as np


def q1():
    arr = np.arange(0, 101)
    arr[1::2] = -1
    print(arr)


def q2():
    arr = np.zeros((20, 20))
    arr[:20, 0] = 1
    arr[:20, 19] = 1
    arr[:1, :19] = 1
    arr[19:20, :19] = 1
    print(arr)


def q3():
    arr = np.random.randint(1, 10)
    print(arr)
    arr.sort()
    print(arr)


def q4():
    arr = np.random.randint(1, 10)
    whatever = np.where(arr == arr.max())
    arr[whatever] = 0
    print(arr)


def q5(value):
    array = np.random.randint(0, 1001, 10)
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    print(array[idx])


q5(5)