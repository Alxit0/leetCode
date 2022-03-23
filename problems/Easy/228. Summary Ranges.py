from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    intervals = []
    a = nums.pop(0)
    temp = f"{a}"
    for i in nums:
        if a + 1 != i:
            intervals.append(temp+f"->{a}"*(str(a) != temp))
            temp = f"{i}"
        a = i
    intervals.append(temp+f"->{a}"*(str(a) != temp))
    return intervals


def main():
    a = [0, 2, 3, 4, 5, 7, 9]
    print(summaryRanges(a))


if __name__ == '__main__':
    main()
