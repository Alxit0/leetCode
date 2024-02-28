class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

def test(fun, case, res):
    sol = fun(*case)

    if res == sol:
        print("OK")
    else:
        print(f"{case = }")
        print(f"{sol = }")
        print(f"{res = }")
        print()

def main():
    s = Solution()
    
    test(
        s.strStr,
        ("sadbutsad", "sad"),
        0
    )
    test(
        s.strStr,
        ("leetcode", "leeto"),
        -1
    )


if __name__ == "__main__":
    main()
