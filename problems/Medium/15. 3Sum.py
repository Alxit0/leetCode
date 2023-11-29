from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resp = set()
        tam = len(nums)

        for i in range(tam-2):
            k = tam-1
            for j in range(i+1, tam):
                soma = nums[i] + nums[j] + nums[k]
                while soma > 0 and k > j:
                    soma -= nums[k]
                    k -= 1
                    soma += nums[k]
                
                if soma == 0 and k != j:
                    resp.add((nums[i], nums[j], nums[k]))
        
        return list(map(list, resp))


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))