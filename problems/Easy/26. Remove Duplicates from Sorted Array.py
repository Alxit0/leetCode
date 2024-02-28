from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            
            n += 1
            nums[n] = nums[i]

        return n + 1


def test(fun, case, res):
    sol = fun(case)

    if res[1] == case[:sol]:
        print("OK")
    else:
        print(f"{case = }")
        print(f"{case[:sol] = }")
        print(f"{res[1] = }")
        print()

def main():
    s = Solution()
    
    test(
        s.removeDuplicates,
        [1,1,2],
        (2, [1, 2])
    )
    test(
        s.removeDuplicates,
        [0,0,1,1,1,2,2,3,3,4],
        (5, [0,1,2,3,4]),
    )


if __name__ == "__main__":
    main()
