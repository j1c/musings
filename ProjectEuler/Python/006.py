__author__ = 'Jaewon'


def square_sums(x):
    sums = 0
    for i in range(1, x + 1):
        sums += i**2
    return sums


def square_of_sums(x):
    sums = 0
    for i in range(1, x + 1):
        sums += i
    return sums**2


if __name__ == '__main__':
    print(square_of_sums(100) - square_sums(100))
