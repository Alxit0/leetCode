from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                return [d[nums[i]], i]


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum(nums=[-1, -2, -3, -4, -5], target=-8))
