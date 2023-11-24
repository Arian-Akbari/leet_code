from collections import defaultdict
from typing import List


def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    groups = defaultdict(list)
    for i in range(len(nums)-1, -1 , -1):
        for j in range (len(nums[i])):
            code = i + j
            groups[code].append(nums[i][j])
    ans = []
    curr = 0
    while curr in groups:
        ans.extend(groups[curr])
        curr += 1
    return ans


print(findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
