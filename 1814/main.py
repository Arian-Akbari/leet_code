from collections import defaultdict
from typing import List


def countNicePairs(nums: List[int]) -> int:
    MOD = 10 ** 9 + 7
    diff = []
    for i in range(len(nums)):
        diff.append(nums[i] - int(str(nums[i])[::-1]))
    count = 0
    dic = {}
    for i in diff:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        val = dic[i]
        count = (count + int(val * (val - 1) / 2)) % MOD
    return count


print(countNicePairs([13, 10, 35, 24, 76]))
