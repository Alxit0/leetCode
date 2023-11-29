from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # sort the array -> min_n, max_n
        a, *_, b = sorted(nums) 

        # find gcd

        for i in range(b, -1, -1):
            if a%i == b%i == 0:
                return i

        return 1
