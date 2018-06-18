__author__ = 'Jaewon'


def is_prime(x):
    if x <= 3:
        return True
    elif x >= 4 and x % 2 == 0:
        return False
    else:
        l = range(3, x, 2)  # Step is 2 since all prime numbers are odd
        for i in l:
            if x % i == 0:
                return False  # if divisible, then not prime.
                break
        return True  # if not divisible by anything, then is prime.


def find_prime(x):  # x is xth number of prime
    primes = 1
    n = 3

    while primes != x:
        if is_prime(n):
            primes += 1
            n += 2
        else:
            n += 2
    return n - 2


if __name__ == '__main__':
    print(find_prime(10001))
