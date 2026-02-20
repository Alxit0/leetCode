class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        cur_dividend = abs(dividend)
        cur_divisor = abs(divisor)
        
        n = 0
        while cur_dividend >= cur_divisor:
            cur_dividend -= cur_divisor
            n += 1

        if (dividend < 0) ^ (divisor < 0):
            n = -n
        return n
    


def test(fun, case, res):

    sol = fun(*case)

    if sol == res:
        print("OK")
    else:
        print(f"{case = }")
        print(f"{sol = }")
        print(f"{res = }")
        print()

def main():
    s = Solution()
    
    test(s.divide, (10, 3), 3)
    test(s.divide, (7, -3), -2)
    test(s.divide, (0, 1), 0)
    test(s.divide, (1, 1), 1)
    test(s.divide, (-2147483648, -1), 2147483648)


if __name__ == "__main__":
    main()
