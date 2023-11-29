from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_v = 0
        resp = []

        for i in nums:
            cur_v += i
            resp.append(cur_v)
        
        return resp
