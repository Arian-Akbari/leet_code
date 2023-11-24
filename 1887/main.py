from typing import List


def reductionOperations(nums: List[int]) -> int:
    nums.sort()
    cost = 0
    count = 0
    current = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        count += 1
        if nums[i] != current:
            cost += count
            current = nums[i]
    return cost


print(reductionOperations([5, 1, 3]))
