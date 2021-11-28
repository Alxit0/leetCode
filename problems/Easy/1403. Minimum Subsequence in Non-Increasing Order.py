from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        r = []
        while len(nums) > 0:
            r += nums.pop(),
            if sum(r) > sum(nums):
                break
        return r
