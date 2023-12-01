from typing import List


def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    first_diff = 0
    diff = []
    for i in range(1, len(nums)):
        first_diff += nums[i] - nums[0]
    diff.append(first_diff)
    current_diff = first_diff
    larger = len(nums) - 1
    smaller = -1
    for i in range(1, len(nums)):
        exchange = nums[i] - nums[i - 1]
        larger -= 1
        smaller += 1
        current_diff += exchange * smaller
        current_diff -= exchange * larger
        diff.append(current_diff)
    return diff


print(getSumAbsoluteDifferences([2,3,5]))
