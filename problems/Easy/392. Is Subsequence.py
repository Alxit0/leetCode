class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        if s == "":
            return True
        temp = list(s)
        for i in t:
            if i == temp[0]:
                del temp[0]
                if len(temp) == 0:
                    return True
        return len(temp) == 0


def main():
    a = ""
    b = "ahbgdcd"
    print(Solution.isSubsequence(a, b))


if __name__ == '__main__':
    main()
