__author__ = 'Jaewon'


def multiples_3(x):
    n = x / 3
    multiples = []
    for i in range(1,n+1):
        multiples.append(3*i)
    return multiples


def multiples_5(x):
    n = x / 5
    multiples = []
    for i in range(1,n):
        multiples.append(5*i)
    return multiples


def multiples_15(x):
    n = x / 15
    multiples = []
    for i in range(1,n+1):
        multiples.append(15*i)
    return multiples

def sum_of_multiples(x,y,z):

    return sum(x) + sum(y) - sum(z)

print sum_of_multiples(multiples_3(1000),multiples_5(1000),multiples_15(1000))

print multiples_3(1000)
print multiples_5(1000)
print multiples_15(1000)
