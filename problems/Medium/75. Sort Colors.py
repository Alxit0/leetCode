from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b = [0, 0, 0]
        for i in nums:
            b[i]+=1
        
        res = [0]*b[0] + [1]*b[1] + [2]*b[2]
        for i in range(len(nums)):
            nums[i] = res[i]
        