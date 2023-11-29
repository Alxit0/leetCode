class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s

		tam = len(s)
		a = ""

		for i in range(numRows):
			j = i
			while i < tam:
				a += s[i]
				
				next_idx = i + (numRows - j - 1)*2
				if j not in (0, numRows-1) and next_idx < tam:
					a += s[next_idx]
				
				i += 2*numRows - 2

		return a


"""
"PAYPALISHIRINGFORGOOGLE"

##### 5
P       H       R
A     S I     O G
Y   I   R   F   O   E
P L     I G     O L
A       N       G

[0, 8, 16]
[1, 7, 9, 15, 17], 6
[2, 6, 10, 14, 18], 4
[3, 5, 11], 2

"""
"""
##### 4
P     I     N
A   L S   I G
Y A   H R
P     I

[0, 6, 12]
[1, 5, 7, 11, 13], 4
[2, 4, 8, 10], 2
"""
Solution().convert("PAYPALISHIRING", 4)
Solution().convert("PAYPALISHIRINGFORGOOGLE", 5)
Solution().convert("A", 1)