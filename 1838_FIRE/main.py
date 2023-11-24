from typing import List


def maxFrequency(nums: List[int], k: int) -> int:
    nums.sort()
    left = 0
    current = 0
    for right in range(len(nums)):
        target = nums[right]
        current += target
        if (right - left + 1) * target - current > k:
            current -= nums[left]
            left += 1
    return len(nums) - left


print(maxFrequency([1, 2, 4, 5, 5, 5, 5, 5, 5, 6], 5))
