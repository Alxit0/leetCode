class Solution:
    table = [
        (1000, 'M'), 
        (900, 'CM'), 
        (500, 'D'), 
        (400, 'CD'), 
        (100, 'C'), 
        (90, 'XC'), 
        (50, 'L'), 
        (40, 'XL'), 
        (10, 'X'), 
        (9, 'IX'), 
        (5, 'V'), 
        (4, 'IV'), 
        (1, 'I')
    ]

    def intToRoman(self, num: int) -> str:

        s = ''
        for val, rom in self.table:
            while num - val >= 0:
                num -= val
                s += rom

        return s

print(Solution().intToRoman(3))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
