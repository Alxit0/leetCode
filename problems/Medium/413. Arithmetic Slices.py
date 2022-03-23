from typing import List


"""
3 - 1
4 - 3
5 - 6
6 - 10
7 - 15
"""


class Solution:
    @staticmethod
    def numberOfArithmeticSlices(nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        tam_atual = 2
        dif = nums[1] - nums[0]
        temp = nums[1]
        resp = 0
        for i in nums[2:]:
            if i - temp == dif:
                tam_atual += 1
            else:
                if tam_atual > 2:
                    resp += tam_atual * (tam_atual + 1) // 2 - (2*tam_atual - 1)
                tam_atual = 2
            dif = i - temp
            temp = i
        # print(tam_atual)
        if tam_atual > 2:
            resp += tam_atual * (tam_atual + 1) // 2 - (2*tam_atual - 1)
        return resp


def main():
    a = [1, 2, 3, 4,]
    print(Solution.numberOfArithmeticSlices(a))


if __name__ == '__main__':
    main()
