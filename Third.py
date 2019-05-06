from pandas import Series, DataFrame, read_csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from random import randint


# obj = Series([3, 6, 9, 12])
# print(obj)
# names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
# births = [968, 155, 77, 578, 973]
# zipped = list(zip(names, births))
# zipped = pd.DataFrame(data=zipped, columns=['Names', 'Births'])
# print(zipped['Names'])
# zipped.to_csv('births1880.csv', index=False, header=False)
# zipped = pd.read_csv(r'births1880.csv')


def q1():
    arr = np.array([[3, 1], [1, 2]])
    arr2 = np.array([9, 8])
    print(np.linalg.solve(arr, arr2))


def q2():
    a = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    print(a)


def q3():
    lang = ["java", "python", r"c#"]
    print(list(filter(lambda x: x == "python", lang)))


def q4():
    a = [(i, i/4184) for i in [5000, 8000, 10000, 6000, 12000]]
    print(a)

q3()
