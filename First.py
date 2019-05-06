import random


def q1():
    my_movies = ['How I Met Your Mother', 'Friends', 'Silicon Valley',
                 'Family Guy', 'South Park', 'Rick and Morty',
                 'Breaking Bad', 'Game of Thrones', 'The Wire']
    for name in my_movies:
        current_movie = name
        str(current_movie).replace(" ", "")
        print("the title " + str(name) + " is " + str(len(name)) + " characters long")


def q2():
    for num in range(1, 100):
        if num % 3 == 0:
            if num % 5 == 0:
                print("BimBamBom")
            else:
                print("boom!!")
        elif num % 5 == 0:
            if num % 3 == 0:
                print("BimBamBom")
            else:
                print("bim")
        else:
            print(num)


def q3():
    maxi = 100
    mini = 0
    answer = input("is your age 51? ")
    while not (answer.startswith('y')):
        if answer == "less":
            maxi = (maxi + mini + 1) / 2
        elif answer == "more":
            mini = (maxi + mini + 1) / 2
        answer = input("is your age " + str((maxi + mini + 1) / 2) + "?")
    print("YOUR AGE IS " + str((maxi + mini + 1) / 2))


def q4():
    test = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},
            1000,
            2000,
            3000,
            ['hat', 't-shirt', 'jeans', {'socks1': 'red', 'socks2': 'blue'}]]
    print(test[2])
    print(test[0])
    print(test[4])
    print(test[0]['Arizona'])
    print(test[4][2])
    print(test[4][3]['socks2'])


def q5():
    num = random.randint(1000, 10000)
    print(num)
    counter = 1
    guess = input("Your 4 digit guess: ")
    arr = []
    while not num == int(guess):
        for digit in range(4):
            if str(guess)[digit] == str(num)[digit]:
                arr.append("X")
            else:
                arr.append(str(guess)[digit])
        print(arr)
        arr.clear()
        guess = input("Your 4 digit guess: ")
        counter += 1
    print("YOU WIN!!!\n" + "THE NUMBER WAS: " + str(num) + "\nIT TOOK YOU " + str(counter) + " GUESSES")


def get_min(arr):
    mini = arr[0]
    for i in arr:
        if i < mini:
            mini = i
    print(mini)


get_min([1, 1, -1, 4])
