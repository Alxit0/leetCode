from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue

            nums[k] = nums[i]
            k += 1
        
        return k



def test(fun, case, res):
    sol = fun(*case)

    if sorted(res[1]) == sorted(case[0][:sol]):
        print("OK")
    else:
        print(f"{case = }")
        print(f"{case[0][:sol] = }")
        print(f"{res[1] = }")
        print()

def main():
    s = Solution()
    
    test(
        s.removeElement,
        ([3,2,2,3], 3),
        (2, [2,2])
    )
    test(
        s.removeElement,
        ([0,1,2,2,3,0,4,2], 2),
        (5, [0,1,4,0,3]),
    )


if __name__ == "__main__":
    main()
