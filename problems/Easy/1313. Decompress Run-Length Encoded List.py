from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        resp = []
        for i in range(0, len(nums), 2):
            a, b = nums[i], nums[i+1]
            resp += [b]*a
        return resp
