from typing import List


def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    result = []
    for i in range(len(l)):
        left = l[i]
        right = r[i]
        temp = []
        for j in range(left, right + 1):
            temp.append(nums[j])
        temp.sort()
        if len(temp) > 1:
            diff = temp[1] - temp[0]
            flag = False
            for k in range(1, len(temp) - 1):
                if temp[k + 1] - temp[k] != diff:
                    flag = True
                    break
            if not flag:
                result.append(True)
            else:
                result.append(False)
        else:
            result.append(True)
    return result


print(checkArithmeticSubarrays([10, -10, -5, 12, 8, -16, -4, -12, -8, 12, 9, -3], [1, 7, 3, 2, 6, 5],
                               [2, 10, 6, 3, 9, 8]))
