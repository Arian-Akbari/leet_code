from typing import List


def minPairSum(nums: List[int]) -> int:
    nums.sort()
    results = []
    length = len(nums)
    for i in range(int(length / 2)):
        sum = nums[i] + nums[length-1-i]
        results.append(sum)
    return max(results)

print(minPairSum([3,5,2,3]))
