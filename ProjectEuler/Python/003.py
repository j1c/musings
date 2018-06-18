__author__ = 'Jaewon'


def is_prime(x):
    if x <= 3:
        return True
    else:
        l = range(3, x, 2)  # Step is 2 since all prime numbers are odd
        for i in l:
            if x % i == 0:
                return False  # if divisible, then not prime.
                break
        return True  # if not divisible by anything, then is prime.


def largest_prime(x):
    if x < 3:
        return x
    else:
        primes = []
        i = 3
        while x != 1:  # stop once we find last prime
            if x % i == 0:
                primes.append(i)
                x /= i  # once prime divides x, change x to new division
            i += 2
        return max(primes)


if __name__ == '__main__':
    print(largest_prime(600851475143))
