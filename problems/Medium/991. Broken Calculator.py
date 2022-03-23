def brokenCalc(startValue: int, target: int) -> int:
    i = 0
    while target > startValue:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        i += 1
    return i + startValue - target


def main():
    a = 3
    b = 2
    print(brokenCalc(a, b))


if __name__ == '__main__':
    main()
