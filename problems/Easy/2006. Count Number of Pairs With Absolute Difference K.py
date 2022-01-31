from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        r = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    r += 1
        return r
