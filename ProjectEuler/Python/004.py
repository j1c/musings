__author__ = 'Jaewon Chung'


def palindrome():  # Start top down to find the largest first.
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            s = str(i * j)
            if s == s[::-1]:
                palindromes.append(i * j)
                #print(i * j)
                #break
    return max(palindromes)


if __name__ == '__main__':
    answer = palindrome()
    print(answer)
