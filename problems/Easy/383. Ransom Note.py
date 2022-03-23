def canConstruct(ransomNote: str, magazine: str) -> bool:
    d = {}
    for i in magazine:
        if i not in d:
            d[i] = 0
        d[i] += 1

    for i in ransomNote:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1

    print(d)
    return all(i >= 0 for i in d.values())


def main():
    a = 'aab'
    b = 'ab'
    print(canConstruct(a, b))


if __name__ == '__main__':
    main()
