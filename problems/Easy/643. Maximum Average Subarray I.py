from typing import  List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp = sum(nums[:k])
        m = temp/k
        for i in range(0, len(nums)-k):
            #print(nums[i:i+k])
            temp -= nums[i] - nums[i+k]
            m = max(m, temp/k)
        return m
