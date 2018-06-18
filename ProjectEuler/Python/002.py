__author__ = 'Jaewon'


def fibonacci(x):
    f1 = 1  # starting numbers are 1 and 2
    f2 = 2
    numbers = []

    while f2 <= x:
        if f2 % 2 == 0:
            numbers.append(f2)
        f2 += f1  # new f2 is sum of two current numbers
        f1 = f2 - f1  # new f1 is difference of new f2 and f1
    return numbers


if __name__ == '__main__':
    print(sum(fibonacci(4000000)))
