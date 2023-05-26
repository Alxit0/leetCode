from typing import List


class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		tam = len(nums)

		resp = nums[0] + nums[1] + nums[2]

		for i in range(tam-2):
			j = i+1
			k = tam-1

			while j != k:
				cur_val = nums[i] + nums[j] + nums[k]
				
				if cur_val == target:
					return target
				elif cur_val < target:
					j += 1
				else:
					k -= 1

				if abs(cur_val - target) < abs(resp - target):
					resp = cur_val
		
		return resp





if __name__ == "__main__":
	nums = [2,3,8,9,10]
	target = 16
	print(Solution().threeSumClosest(nums, target))