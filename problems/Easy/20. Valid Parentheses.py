def isValid(s: str) -> bool:
    stack = []
    op = "{[("
    cl = "}])"
    d = dict(zip(cl, op))
    print(d)
    for i in s:
        if i in op:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            atual = stack.pop()
            if op.index(d[i]) != op.index(atual):
                return False
        # print(stack)
    return stack == []


def main():
    a = "]"
    print(isValid(a))


if __name__ == '__main__':
    main()