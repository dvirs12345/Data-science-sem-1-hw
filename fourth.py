import pandas as pd
import numpy as np


def q1():
    drinks_file = pd.read_csv("drinks.csv")
    euc = drinks_file.loc[drinks_file['continent'] == 'EU']
    print(np.mean(euc)['beer_servings'])
    print(np.mean(drinks_file.loc[drinks_file['continent'] == 'AS'])['beer_servings'])
    print(np.mean(drinks_file.loc[drinks_file['continent'] == 'AF'])['beer_servings'])
    print(np.mean(drinks_file.loc[drinks_file['continent'] == 'NA'])['beer_servings'])
    print(np.mean(drinks_file.loc[drinks_file['continent'] == 'OC'])['beer_servings'])
    print(np.mean(drinks_file.loc[drinks_file['continent'] == 'SA'])['beer_servings'])


def q1b():
    drinks_file = pd.read_csv("drinks.csv")
    print(pandas.DataFrame.describe(drinks_file.loc[drinks_file['continent'] == 'AS'])['wine_servings'])


def q1c():
    drinks_file = pd.read_csv("drinks.csv")
    print(np.mean(np.mean(drinks_file)))


def q1d():
    drinks_file = pd.read_csv("drinks.csv")
    arr = []
    for i in drinks_file.loc[drinks_file['continent'] == 'AS']['total_litres_of_pure_alcohol']:
        arr.append(i)
    print(np.median(arr))
    # print(np.median(drinks_file.loc[drinks_file['continent'] == 'AS'])['total_litres_of_pure_alcohol'][1])


def q1e():
    drinks_file = pd.read_csv("drinks.csv")
    print(np.mean(drinks_file['spirit_servings']))
    print(np.max(drinks_file['spirit_servings']))
    print(np.min(drinks_file['spirit_servings']))


def q2a():
    cars_file1 = pd.read_table("cars1.csv")
    cars_file1.drop(cars_file1.columns[cars_file1.columns.str.contains('unnamed', case=False)], axis=1)


def q2b():
    cars_file1 = pd.read_csv("cars1.csv")
    print(cars_file1.columns)


def q2c():
    cars_file1 = pd.read_table("cars1.csv")
    cars_file2 = pd.read_table("cars2.csv")
    x = [cars_file1, cars_file2]
    result = pd.concat(x, sort=True)
    print(result)
q2c()
