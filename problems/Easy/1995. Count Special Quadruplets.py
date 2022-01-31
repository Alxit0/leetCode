from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        l = len(nums)
        r = 0
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    for m in range(k+1, l):
                        if nums[i] + nums[j] + nums[k] == nums[m]:r+=1
        return r