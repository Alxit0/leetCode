class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = ''
        p = 1
        for i in range(0, len(s), k):
            a += s[i:i + k][::(-1) ** p]
            p += 1

        return a


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))  # bacdfeg
    print(s.reverseStr("abcd", 2))  # bacd
