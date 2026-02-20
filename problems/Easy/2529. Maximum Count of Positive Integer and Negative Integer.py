from typing import List


class Solution:
    def _helper(self, nums: List[int], count: int) -> int:
        a, b = 0, len(nums) - 1

        while a < b:
            p = a + (b - a) // 2

            if nums[p] < 0:
                a = p + 1
            else:
                b = p
            


    def maximumCount(self, nums: List[int]) -> int:
        pass


print(Solution().maximumCount([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))