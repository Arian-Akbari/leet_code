from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0
    while l < r:
        area = (r - l) * min(height[r], height[l])
        max_area = max(area, max_area)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
