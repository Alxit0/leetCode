class MyQueue:
    def __init__(self):
        self.ls = []

    def push(self, x: int) -> None:
        self.ls.append(x)

    def pop(self) -> int:
        return self.ls.pop(0)

    def peek(self) -> int:
        return self.ls[0]

    def empty(self) -> bool:
        return len(self.ls) == 0


def main():
    # ????
    pass


if __name__ == '__main__':
    main()
