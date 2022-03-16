import re
class Solution:
    @staticmethod
    def isMatch(self, s: str, p: str) -> bool:
        seq = list(s)
        patterns = []
        temp = ''
        print(p[::-1])
        for i in p[::-1]:
            if len(patterns) > 1 and len(patterns[0]) == 2 and patterns[0][1] == i:
                temp = ''
                continue
            temp += i

            if i != '*':
                patterns.insert(0, temp)
                temp = ''
        print(patterns)

        for i in patterns:
            if len(seq) == 0:
                return False
            if len(i) == 1:
                if seq[0] == i or i == '.':
                    seq.pop(0)
                else:
                    return False
            else:
                while len(seq) > 0 and (seq[0] == i[1] or i[1] == '.'):
                    seq.pop(0)
        # print(seq)
        return len(seq) == 0


def main():
    a = "aa"
    b = "a*a"
    print(b)
    print(Solution.isMatch(0, a, b))
    # print(bool(re.fullmatch(b, a)))


if __name__ == '__main__':
    main()
