class Solution:
	def tribonacci(self, n: int) -> int:
		a, b, c = 0, 1, 1

		for _ in range(n):
			a, b, c = b, c, a+b+c
		
		return a

class Solution2:
	def tribonacci(self, n: int, memo=None) -> int:
		if memo is None:
			memo = [0, 1, 1] + [-1]*(n-2)
		
		if memo[n] != -1:
			return memo[n]

		resp = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
		memo[n] = resp
		return resp


if __name__ == "__main__":
	n = 29

	print(Solution2().tribonacci(n))
	print(Solution().tribonacci(n))
