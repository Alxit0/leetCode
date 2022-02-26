from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        del nums1[-1]
    p = 0
    for i in nums2:
        while p != len(nums1) and i > nums1[p]:
            p += 1
        nums1.insert(p, i)
        # print(nums1)


def main():
    a = [1, 2, 3, 0, 0, 0]
    m = 3
    b = [2, 5, 6]
    n = 3
    print(a)
    merge(a, m, b, n)
    print(a)


if __name__ == '__main__':
    main()
