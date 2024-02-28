from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            r ^= i
        
        return r
    

def test(fun, case, res):

    sol = fun(case)

    if sol == res:
        print("OK")
    else:
        print(f"{case = }")
        print(f"{sol = }")
        print(f"{res = }")
        print()

def main():
    s = Solution()
    
    test(
        s.singleNumber,
        [2,2,1],
        1
    )
    test(
        s.singleNumber,
        [4,1,2,1,2],
        4
    )
    test(
        s.singleNumber,
        [1],
        1
    )


if __name__ == "__main__":
    main()
