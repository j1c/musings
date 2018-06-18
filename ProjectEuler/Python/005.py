"""
The smallest multiple is when the factors of all numbers below 20 are multiplied.

EX: for 10 - you need numbers 2,3,3,4,5,7 = 2520
"""


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


def generate_primes(x):  # Returns all prime numbers less than x.
    primes = [2]
    number = 3
    while max(primes) < x:
        if is_prime(number):
            primes.append(number)
        number += 2
    return primes


def find_prime_factors(x):  # Returns prime factors of x
    primes = generate_primes(x)
    factors = []
    i = 0
    while x != 1:
        if x % primes[i] == 0:
            factors.append(primes[i])
            x /= primes[i]
            i = 0  # Some numbers can be divided by 2 or 3 multiple times. So reset i.
        else:
            i += 1  # If primes[i] is not a factor, try next prime.
    return factors


def find_factors(x):  # Returns prime factors for all numbers <= x.
    factors = []
    for i in range(1, x + 1, 1):
        if is_prime(i):
            factors.append(i)
        else:
            l = find_prime_factors(i)
            for j in l:
                if factors.count(j) > l.count(
                        j
                ):  # Checking if more factors are in factors than in l.
                    continue
                else:
                    while factors.count(j) != l.count(j):
                        factors.append(j)
    return factors


if __name__ == '__main__':
    mult = 1
    for i in find_factors(20):
        mult *= i

    print(mult)
