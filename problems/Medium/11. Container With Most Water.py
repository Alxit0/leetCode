from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    ans = 0
    while left < right:
        ans = max(ans, min(height[left], height[right])*(right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans


def main():
    a = [1, 1]
    print(maxArea(a))


if __name__ == '__main__':
    main()
