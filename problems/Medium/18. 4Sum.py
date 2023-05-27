from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		if len(nums) < 4:
			return []
		
		resp = set()
		nums = sorted(nums)
		tam = len(nums)
		
		for i in range(tam-3):
			for j in range(i+1, tam-2):
				
				k = j+1
				l = tam-1
			
				
				while k != l:
					cur_val = nums[i] + nums[j] + nums[k] + nums[l]

					if cur_val == target:
						resp.add((nums[i], nums[j], nums[k], nums[l]))
						k+=1
					elif cur_val < target:
						k += 1
					else:
						l -= 1
		
		return list(map(list, resp))


if __name__ == "__main__":
	nums = [-3,-2,-1,0,0,1,2,3]
	target = 0

	print(Solution().fourSum(nums, target))
