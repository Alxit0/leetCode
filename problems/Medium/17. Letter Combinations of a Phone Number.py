from typing import List


class Solution:
	d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

	def letterCombinations(self, digits: str) -> List[str]:
		resp = [""]

		for i in map(int, digits):
			temp = []
			for j in resp:
				for k in self.d[i-2]:
					temp.append(j+k)
			
			resp = temp
		
		if len(resp) == 1:
			return []
		
		return resp


if __name__ == "__main__":
	digits = "22"

	print(Solution().letterCombinations(digits))