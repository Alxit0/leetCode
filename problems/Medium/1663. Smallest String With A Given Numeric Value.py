def getSmallestString(n: int, k: int) -> str:
    resp = ""
    while k > n != 0:
        temp = min(26, k - n + 1)
        resp += chr(temp + 96)

        k -= temp
        n -= 1

    return "a" * n + resp[::-1]


def main():
    a = 3
    b = 27
    print(getSmallestString(a, b))


if __name__ == '__main__':
    main()
