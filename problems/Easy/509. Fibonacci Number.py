
class Solution:
	memo = {
		0: 0,
		1: 1
	}

	def fib(self, n: int) -> int:
		if n in self.memo:
			return self.memo[n]
		
		resp = self.fib(n-1) + self.fib(n-2)
		self.memo[n] = resp
		return resp

if __name__ == "__main__":
	n = 4

	print(Solution().fib(n))
