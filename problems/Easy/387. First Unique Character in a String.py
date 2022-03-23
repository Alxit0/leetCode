def firstUniqChar(s: str) -> int:
    temp = []
    bl = set()
    for i in s:
        if i in temp:
            temp.remove(i)
            bl.add(i)
        elif i not in bl:
            temp.append(i)
    return s.index(temp[0]) if temp else -1


def main():
    a = "leetcode"
    print(firstUniqChar(a))


if __name__ == '__main__':
    main()
