class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        temp = []
        cnt = 0
        for i in s:
            temp += '',
            for j in range(len(temp)-1, -1, -1):
                if i in temp[j]:
                    cnt = max(cnt, len(temp[j]))
                    del temp[j]
                else:
                    temp[j] += i
            # print(temp)
        cnt = max(cnt, *map(len, temp))
        return cnt


if __name__ == '__main__':
    a = Solution()
    print(a.lengthOfLongestSubstring(" "))