def mapear(seq):
    d = {}
    for i in seq:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d


def isAnagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)
    return mapear(s) == mapear(t)


def main():
    a = "anagram"
    b = "nagaram"
    print(isAnagram(a, b))


if __name__ == '__main__':
    main()
