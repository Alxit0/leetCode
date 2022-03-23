from typing import List


def find(lista: List[int], target: int) -> int:
    for i in range(len(lista)):
        if target == lista[i]:
            return i
    return -1


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    resp = []
    for i in nums2:
        temp = find(nums1, i)
        if temp > -1:
            resp.append(i)
            del nums1[temp]
    return resp


def main():
    a = [1, 2, 2, 1]
    b = [2, 2]
    print(intersect(a, b))


if __name__ == '__main__':
    main()
