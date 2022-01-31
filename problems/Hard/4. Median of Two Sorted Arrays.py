from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1+nums2)
        p = len(a)/2
        if p%1:return a[int(p)]
        else: return (a[int(p)]+a[int(p)-1])/2