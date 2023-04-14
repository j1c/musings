# https://cses.fi/problemset/task/1068

n = int(input())

out = str(n)

while n != 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    out += " " + str(int(n))

print(out)
