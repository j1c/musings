# https://cses.fi/problemset/task/1634

n, x = [int(i) for i in input().split(" ")]
coins = [int(i) for i in input().split(" ")]

if x == 0:
    print(0)
else:
    # dynamic programming
    minimum_coins = [0]

    for value in range(1, x + 1):
        best = 10000000
        for coin in coins:
            if value - coin >= 0:
                best = min(best, minimum_coins[value - coin] + 1)

        minimum_coins.append(best)

    if minimum_coins[-1] == 10000000:
        print(-1)
    else:
        print(minimum_coins[-1])
